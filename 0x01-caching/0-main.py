#!/usr/bin/python3

""" 0-main """

BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

# added tests
print("="*20)
my_cache.put(None, "Do not add it")
my_cache.put('key', None)
my_cache.print_cache()
print(my_cache.get("missing"))
print(my_cache.get(None))
