#!/usr/bin/env python3
""" module docs """
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorate function """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ callable function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ docorate function """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(func: Callable) -> None:
    """Display the history of calls of a particular function."""
    func_name = func.__qualname__
    the_inp_key = f"{func_name}:inputs"
    the_out_key = f"{func_name}:outputs"
    redis_conn = redis.Redis()
    num_calls = min(redis_conn.llen(the_inp_key), redis_conn.llen(the_out_key))
    print(f"{func_name} was called {num_calls} times:")
    for i in range(num_calls):
        input_val = redis_conn.lindex(the_inp_key, i).decode('utf-8')
        output_val = redis_conn.lindex(the_out_key, i).decode('utf-8')
        print(f"{func_name}(*{input_val}) -> {output_val}")


class Cache:
    """ clas Cach """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
