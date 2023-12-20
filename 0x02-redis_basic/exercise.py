#!/usr/bin/env python3
import redis
from typing import Any
import uuid


class Cache():
    """initialize redis client,flush db on init and store data into redis"""
    def __init__(self) -> None:
        """initialize redis client and flash on initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """generate randomkey and use it to store data. returning the key"""
        random_key = str(uuid.uuid4())

        self._redis.set(random_key, data)
        return random_key
