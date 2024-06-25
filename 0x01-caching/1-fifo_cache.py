#!/usr/bin/env python3

"""
This module implements a First-In-First-Out (FIFO) cache
using the BaseCaching class.
"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initializes an instance of the FIFOCache class.
        """
        super().__init__()
        self.__fifo = deque([])

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        if key is not None and item is not None:
            # If the key exists in the cache
            if key in self.cache_data:
                self.cache_data[key] = item
                self.__fifo.remove(key)
                self.__fifo.appendleft(key)
                return
            # If the key does not exist in the cache
            self.__fifo.appendleft(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                removed_key = self.__fifo.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None
                if the key does not exist in the cache.
        """
        return self.cache_data.get(key, None)
