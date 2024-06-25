#!/usr/bin/env python3

"""
This module implements a LRUCache
using the BaseCaching class as its base.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.

    Implements a Least Recently Used (LRU) caching algorithm.

    Attributes:
        __lru (OrderedDict): A dictionary that keeps track
            of the least recently used items.

    Methods:
        put(key, item): Adds an item to the cache.
        get(key): Retrieves an item from the cache.
    """

    def __init__(self):
        """
        Initialize an instance of LIFOCache.
        """
        super().__init__()
        self.__lru = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.

        If the key already exists in the cache, the item is updated
        and moved to the end of the LRU list.
        If the key does not exist in the cache and the cache is full,
        the least recently used item is removed.
        The new item is then added to the cache and the LRU list.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            # If the key exists in the cache
            if key in self.cache_data:
                self.cache_data[key] = item
                self.__lru[key] = item
                self.__lru.move_to_end(key, last=True)
                return
            # If the key does not exist in the cache
            if len(self.cache_data) == self.MAX_ITEMS:
                del_key, _ = self.__lru.popitem(last=False)
                print("DISCARD: {}".format(del_key))
                del self.cache_data[del_key]
            self.cache_data[key] = item
            self.__lru[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.

        If the key exists in the cache, the item is moved
        to the end of the LRU list.
        If the key does not exist in the cache, None is returned.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
                does not exist in the cache.
        """
        if key in self.cache_data:
            self.__lru.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
