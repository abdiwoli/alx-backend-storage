#!/usr/bin/env python3
"""task 11"""


def schools_by_topic(mongo_collection, topic):
    """ return all the list with spesific topic"""
    return mongo_collection.find({"topic": topic})
