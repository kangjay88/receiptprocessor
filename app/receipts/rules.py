import datetime
import decimal
import math
from app.models import Receipt

class RetailAlphaNumericRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        points = 0
        for c in receipt.retailer:
            if c.isalnum():
                points += 1
        
        return points

class TotalRoundDollarRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        points = 50 if receipt.total % 1 == 0 else 0
        return points

class TotalMultipleRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        points = 25 if receipt.total % decimal.Decimal(0.25) == 0 else 0
        return points

class ItemCountRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        numItemsHalved = math.floor(len(receipt.items) / 2)
        return numItemsHalved * 5

class DescriptionLengthRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        points = 0
        for item in receipt.items:
            if (len(item.shortDescription.strip()) % 3 == 0):
                points += math.ceil(item.price * decimal.Decimal(0.2))
        
        return points

class PurchaseDateOddRule():
    @staticmethod
    def calculatePoints(receipt : Receipt):
        points = 6 if receipt.purchaseDate.day % 2 == 1 else 0
        return points

class PurchaseTimeRule():
    two_pm = datetime.time(14, 0, 0)
    four_pm = datetime.time(16, 0, 0)

    @staticmethod
    def calculatePoints(receipt : Receipt):
        if receipt.purchaseTime > PurchaseTimeRule.two_pm and receipt.purchaseTime < PurchaseTimeRule.four_pm:
            return 10        
        
        return 0