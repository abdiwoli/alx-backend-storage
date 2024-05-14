// list all documents of school mango
def top_students(mongo_collection):
    flag = [
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return mango_collection.aggregate(flag)
