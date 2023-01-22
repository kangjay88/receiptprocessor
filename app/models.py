from datetime import datetime
from uuid import uuid4

data = []
date = datetime.now()

class Receipt():
    retailer = data.Column(data.String(250), primary_key=True)
    purchase_date = data.Column(data.String(10), nullable = False, default=date.strftime("%Y-%m-%d"))
    purchase_time= data.Column(data.String(10), nullable = False, default=date.strftime("%H:%M"))
    items = data.relationship("Items", backref="items", lazy=True)
    total = data.Column(data.String(10), nullable=False)

    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total

    def createUUID():
        return uuid4(Receipt)

    def get_Item_price(self):
        return

    def to_dict(self):
        return {}

class Item():
    shortDescription = data.Column(data.String(300), nullable=False)
    price: data.Column(data.String(10), nullable=False)

    def __init__(self, shortDescription, price):
        self.shortDescription = shortDescription
        self.price = price