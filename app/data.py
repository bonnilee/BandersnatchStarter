from os import getenv

from certifi import where
from dotenv import load_dotenv
from BloomtechMonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from typing import Iterable, Dict



load_dotenv()


class Database:

    """MongoDB interface for monster data."""

    def __init__(self, collection: str = "monsters"):
        client = MongoClient(getenv("DB_URL"), tlsCAFile=where())
        self.collection = client.get_default_database()[collection]

    def seed(self, count: int = 1000) -> None:
        """Insert `count` randomly generated monsters into the collection."""
        monsters: Iterable[Dict] = (
            Monster().to_dict() for _ in range(count)
        )
        self.collection.insert_many(monsters)

    def reset(self) -> None:
        """Delete all documents from the collection."""
        self.collection.delete_many({})
        

    def count(self) -> int:
        """Return number of documents in the collection."""
        return self.collection.count_documents({})
        

    def dataframe(self) -> DataFrame:
        """Return collection data as a Pandas DataFrame."""
        records = list(self.collection.find({}, {"_id": False}))
        return DataFrame(records)
        

    def html_table(self) -> str | None:
        """Return HTML table of the data, or None if empty."""
        df = self.dataframe()
        if df.empty:
            return None
        return df.to_html(classes="table table-striped", index=False)
        



"""
Database interface for monster data.
Provides methods to seed, reset, count, and visualize data.
"""

