from app.receipts.rules import *

class Points:
    rules = [
        RetailAlphaNumericRule(),
        TotalRoundDollarRule(),
        TotalMultipleRule(),
        ItemCountRule(),
        DescriptionLengthRule(),
        PurchaseDateOddRule(),
        PurchaseTimeRule()
    ]

    @staticmethod
    def calculate(receipt : Receipt):
        points = 0

        for rule in Points.rules:
            points += rule.calculatePoints(receipt)

        return points