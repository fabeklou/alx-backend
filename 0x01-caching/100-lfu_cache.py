#!/usr/bin/env python3

"""
This module implements a LFUCache
using the BaseCaching class as its base.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.

    Implements a Leat Frequently Used (LFU) caching algorithm.

    Attributes:
        __lfu (OrderedDict): A dictionary that keeps track
            of the Leat Frequently Used items.

    Methods:
        put(key, item): Adds an item to the cache.
        get(key): Retrieves an item from the cache.
    """

    def __init__(self):
        """
        Initialize an instance of LFUCache.
        """
        super().__init__()
        self.__lfu = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.

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
                self.__lfu[key] += 1
                self.__lfu.move_to_end(key, last=True)
                return
            # If the key does not exist in the cache
            if len(self.cache_data) == self.MAX_ITEMS:
                # find LFU and LRU (if more than one) and remove it
                lfu_key, lfu_weight = '_', float('+inf')
                for k in self.__lfu.keys():
                    w = self.__lfu[k]
                    if w < lfu_weight:
                        lfu_key, lfu_weight = k, w
                del self.cache_data[lfu_key]
                self.__lfu.pop(lfu_key)
                print("DISCARD: {}".format(lfu_key))
            self.cache_data[key] = item
            self.__lfu[key] = 1

    def get(self, key):
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
                does not exist in the cache.
        """
        if key in self.cache_data:
            self.__lfu[key] += 1
            self.__lfu.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
