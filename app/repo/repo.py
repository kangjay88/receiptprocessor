from app.models import Receipt

class Repo:
    receipt_dict = { }

    @staticmethod
    def store_receipt(receipt : Receipt):
        Repo.receipt_dict[receipt.id] = receipt
        return

    @staticmethod
    def get_receipt(id : int):
        return Repo.receipt_dict.get(id)