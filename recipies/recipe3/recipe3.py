"""
Problem:
--------
  You have a list of dictionaries and you would like to sort the entries
according to one or more of the dictionary values.

Solution:
---------

  Sorting this type of structure is easy using the operator modules's
itemgetter function. Let's say you've queried a database table to get a
listing of the members on you website, and you have receive the following
data structure in return
"""

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004}
]

"""
  It's fairly easy to putput these rows ordered by any of the fields common
to all the dictionaries. For example:
"""

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))

print(rows_by_fname)
print("\n\n")
print(rows_by_uid)
