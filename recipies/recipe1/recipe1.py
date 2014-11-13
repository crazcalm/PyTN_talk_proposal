"""
Source: Python Cookbook, 3rd edition, number 4.14

Problem:
--------

  You have a nested sequence that you want to flatten into a single list of
values

Solution:
---------
  This is easily solved by writing a recursive generator function involving a
yield from statement


Notes:
------

1. Python 2 does not have yield from (check)
"""

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

if __name__ == "__main__":
    items = [1, 2, [3, 4, [5 ,6], 7], 8]
    for x in flatten(items):
        print(x)

