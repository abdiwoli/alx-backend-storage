#!/usr/bin/env python3
""" documentation module """


def top_students(mongo_collection):
    """ to students by average """
    flag = [
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(flag)
