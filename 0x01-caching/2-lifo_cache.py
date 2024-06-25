#!/usr/bin/env python3

"""
This module implements a LIFO (Last-In, First-Out) cache
using the BaseCaching class as its base.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize an instance of LIFOCache.
        """
        super().__init__()
        self.__lifo = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is not None and item is not None:
            # If the key exists in the cache
            if key in self.cache_data:
                self.cache_data[key] = item
                self.__lifo.remove(key)
                self.__lifo.append(key)
                return
            # If the key does not exist in the cache
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                removed_key = self.__lifo.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))
            self.__lifo.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None
                if the key does not exist in the cache.
        """
        return self.cache_data.get(key, None)
