#!/usr/bin/env python3
"""
task 1
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    anything
    """
    def __init__(self):
        """
        anything
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        anything
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", first_key)
        else:
            return

    def get(self, key):
        """
        anything
        """
        return self.cache_data.get(key, None)
