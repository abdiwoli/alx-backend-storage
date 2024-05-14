#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    if (mongo_collection.count_documents({})) == 0:
        return []
    return mongo_collection.find()
