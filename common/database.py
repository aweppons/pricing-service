import pymongo
from typing import Dict, List


class Database:

    URI = "mongodb://10.0.2.6:27017/pricing"
    print("Connected to mongo 10.0.2.6")
    DATABASE = pymongo.MongoClient(URI).get_database()
    print(f"Connected to: {DATABASE}")

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    # @staticmethod
    # def insert(collection: str, data: Dict) -> None:
    #    Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)
