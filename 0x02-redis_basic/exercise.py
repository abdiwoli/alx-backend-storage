#!/usr/bin/env python3
""" module docs """
import redis
import uuid


class Cache:
    """ clas Cach """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
