from abc import ABCMeta, abstractmethod
from common.database import Database
import uuid
from typing import List, TypeVar, Type, Dict

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, _id: str = None, *args, **kwargs):
        self._id = _id or uuid.uuid4().hex

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def get_by_id(cls: Type[T], _id: str):
        return cls(**Database.find_one(cls.collection, {"_id": _id}))

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplemented

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: str) -> T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_by_many(cls: Type[T], attribute: str, value: str) -> List[T]:
        return[cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
