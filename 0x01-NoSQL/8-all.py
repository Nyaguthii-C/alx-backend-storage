#!/usr/bin/python3
"""import python module to establish a connection to a database"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')

    if (mongo_collection.find()):
        return mongo_collection.find()
    else:
        return []
