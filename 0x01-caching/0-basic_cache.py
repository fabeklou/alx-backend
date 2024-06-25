#!/usr/bin/env python3

"""
This module provides a BasicCache class that
inherits from BaseCaching class.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching class.
    """

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key,
                or None if the key is not found.
        """
        return self.cache_data.get(key, None)
