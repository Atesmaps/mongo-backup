#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps - MongoDB Backups **
#
#   An Atesmaps tool to back up MondoDB data and
#   unpload dump to DigitalOcean Spaces.
#
#   Collaborators:
#     - Nil Torrano: ntorrano@atesmaps.org
#     - Atesmaps Team: info@atesmaps.org
#
#   January 2024
#
######################################################
from os import getenv

import bson
from pymongo import MongoClient


class Mongo:
    def __init__(self):
        self.db = self._get_conn(self)

    @staticmethod
    def _get_conn(self) -> MongoClient:
        """Get connection to MongoDB."""
        client = MongoClient(getenv("MONGO_URI"))
        return client[getenv("MONGO_DATABASE")]

    def do_backup(self, output_path: str) -> None:
        """Backup MongoDB database."""
        try:
            for collection in self.db.list_collection_names():
                with open(f"{output_path}/{collection}.bson", "wb+") as f:
                    for document in self.db[collection].find({}):
                        f.write(bson.BSON.encode(document))
        except Exception as exc:
            raise Exception("An error occurred during backup process.") from exc
