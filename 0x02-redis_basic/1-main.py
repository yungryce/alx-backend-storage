#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

# Store the keys and values
stored_values = {}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    stored_values[key] = value
    assert cache.get(key, fn=fn) == value

# Print all keys and their associated values
for key, value in stored_values.items():
    print(f"Key: {key}, Value: {value}")

print("All tests passed!")
