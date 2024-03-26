#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def list_all(mongo_collection):
    """ List all documents in Python """
    count = mongo_collection.count_documents({})

    if count == 0:
        return []

    return mongo_collection.find()
