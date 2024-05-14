#!/usr/bin/env python3
"""change topic 10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """ change sthe topic """
    
    return mongo_collection.update_many(
        {"name":name}, {"$set":{"topics":topics}}
    )
