#!/usr/bin/env python3
""" module docs """
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """ Decorate function """
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        """ callable function """
        self._redis.incr(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


class Cache:
    """ clas Cach """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        if fn is int:
            return self.get_int(key)
        if fn is str:
            return self.get_str(key)
        val = self._redis.get(key)
        if fn and Callable(fn):
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        return int(self._redis.get(key))
