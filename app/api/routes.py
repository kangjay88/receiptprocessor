from flask import Blueprint, json, request, jsonify
from app.models import data, Receipt, Item
from uuid import uuid4

api = Blueprint ('api', __name__, url_prefix='/api')

@api.route('/')
def home():
    return {'hello': 'message'}

@api.route('/receipts/process', methods=['POST'])
def getReceipt():
    with api.open_resource('example.json', 'r') as db: #'r' = open resource json file as 'read-only'
        data = json.load(db)
    return data, 200

@api.route('/receipts/<id>/points', methods=['GET'])
def getIdPoints():
    return 
