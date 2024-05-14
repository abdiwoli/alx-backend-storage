#!/usr/bin/env python3
from pymongo import MongoClient


def nginx_logs_stats():
    """ script that provides some stats about Nginx logs stored in MongoDB"""

    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get count of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method} {count}")

    # Get count of documents with method=GET and path=/status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_logs_stats()
