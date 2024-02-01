#!/usr/bin/env python3
"""
task 0
"""
from base_caching import BaseCaching


class BasicCache (BaseCaching):
    """
    class
    """

    def put(self, key, item):
        """
        anything
        """
        if key and item:
            self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """
        anything
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
