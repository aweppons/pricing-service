import re
import requests
import uuid
from typing import Dict, List
from bs4 import BeautifulSoup
from models.model import Model


class Item(Model):
    collection = "items"

    def __init__(self, url: str, tag: str, query: Dict, _id: str = None):
        super().__init__()
        self.url = url
        self.tag = tag
        self.query = query
        self.price = None
        self.collection = "items"
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        # returns an f-string
        return f"< URL: {self.url}"

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        return self.price

    # Turns item from a python object int something that can be stored in MongoDB
    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag": self.tag,
            "query": self.query
        }








