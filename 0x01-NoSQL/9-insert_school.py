#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """ insert and return inserted id """
    
    return mongo_collection.insert_one(kwargs).inserted_id
