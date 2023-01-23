from typing import List
from typing import Any
from dataclasses import dataclass, field
from datetime import datetime
from datetime import date
from datetime import time
import decimal
from decimal import Decimal

@dataclass
class Item:
    shortDescription: str
    price: decimal

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _shortDescription = str(obj.get("shortDescription"))
        _price = Decimal(str(obj.get("price")))
        return Item(_shortDescription, _price)

@dataclass
class Receipt:
    retailer: str
    purchaseDate: date
    purchaseTime: time
    items: List[Item]
    total: decimal
    id: str = field(init=False)
    points: int = field(init=False)

    @staticmethod
    def from_dict(obj: Any) -> 'Receipt':
        _retailer = str(obj.get("retailer"))
        _purchaseDate = datetime.strptime(str(obj.get("purchaseDate")), "%Y-%m-%d").date()
        _purchaseTime = datetime.strptime(str(obj.get("purchaseTime")), "%H:%M").time()
        _items = [Item.from_dict(y) for y in obj.get("items")]
        _total = Decimal(str(obj.get("total")))
        return Receipt(_retailer, _purchaseDate, _purchaseTime, _items, _total)