from flask import Blueprint, request, jsonify
from app.models import Receipt
from uuid import uuid4
from app.receipts.points import Points

from app.repo.repo import Repo

receipts = Blueprint('receipts', __name__, url_prefix='/receipts')

@receipts.route('/process', methods=['POST'])
def process_receipt():
    # preliminary validation
    if not request.is_json:
        return 'The receipt is invalid', 400
    
    # parse the incoming json
    jsonStr = request.get_json()
    receipt = Receipt.from_dict(jsonStr)

    # generate id
    receipt.id = str(uuid4())

    # calculate points
    receipt.points = Points.calculate(receipt)

    # store in repo
    Repo.store_receipt(receipt)

    # return id
    return jsonify(
        id=receipt.id
    ), 200

@receipts.route('/<id>/points', methods=['GET'])
def get_points(id):
    # lookup the receipt in the repo
    receipt = Repo.get_receipt(id)

    # validate receipt exists
    if receipt is None:
        return 'No receipt found for that id', 404

    # return the points value
    return jsonify(
        points=receipt.points
    ), 200