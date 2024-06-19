#!/usr/bin/env python3
"""Module declares a Redis Cache class with methods
to store and retrieve data."""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


class Cache:
    '''declares a Cache redis class'''
    def __init__(self):
        """Initialize the Redis instance and flush the database."""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key associated with the stored data.
        """
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis and optionally apply a conversion function

        Args:
            key (str): The key of the data to retrieve.
            fn (Optional[Callable], optional): A function to apply to the data.
            Defaults to None.

        Returns:
            Union[str, bytes, int, float]: The retrieved data, optionally
            transformed by `fn`.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieve data from Redis and convert it to a string.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            str: The data converted to a string.
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            int: The data converted to an integer.
            Returns 0 if conversion fails.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
