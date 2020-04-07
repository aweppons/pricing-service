from typing import Dict, List
from models.model import Model
import uuid


class Alert(Model):
    collection = "alerts"

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.item_id = item_id
        self.item = Model.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = "alerts"
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under {self.price_limit}")



