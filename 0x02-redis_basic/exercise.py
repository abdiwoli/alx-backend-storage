#!/usr/bin/env python3
""" module docs """
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """ clas Cach """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(key: str, fn: Optional[Callable]) -> Any:
        if fn is int:
            return self.get_int()
        if fn is str:
            return self.get_str()
        val = self._redis.get(key)
        if fn and Callable(fn):
            return fn(val)
        return val

    def get_str(self) -> str:
        return self._redis.get().decode('utf-8')

    def get_int(self) -> int:
        return int(self._redis.get())
        
        
