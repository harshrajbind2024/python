
print("\n"" 1")
from collections import defaultdict

# Default type is int (default value = 0)
d = defaultdict(int)
d['a'] += 1  # No KeyError, default value is 0
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})

# Default type is list
d_list = defaultdict(list)
d_list['a'].append(10)
print(d_list)  # Output: defaultdict(<class 'list'>, {'a': [10]})





print("\n""2 ")
from collections import OrderedDict

d = OrderedDict()
d['b'] = 2
d['a'] = 1
d['c'] = 3

print(d)  # Output: OrderedDict([('b', 2), ('a', 1), ('c', 3)])

# Move 'a' to the end
d.move_to_end('a')
print(d)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])






print("\n"" 3")
from collections import Counter



print("\n""4 ")
# Count character frequency in a string
c = Counter("banana")
print(c)  # Output: Counter({'a': 3, 'n': 2, 'b': 1})



print("\n""5 ")
# Count words in a list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = Counter(words)
print(word_count)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})



print("\n"" 6")
# Most common elements
print(word_count.most_common(2))  # Output: [('apple', 3), ('banana', 2)]





print("\n""7 ")
d = {}

# Instead of: if 'numbers' not in d: d['numbers'] = []
d.setdefault('numbers', []).append(5)

print(d)  # Output: {'numbers': [5]}





print("\n""8 ")
# Merging Dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

merged = d1 | d2  # Merges, with d2 values overriding d1
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}



print("\n"" 9")
# Dictionary Comprehensions
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



print("\n"" 10")
d = {'b': 2, 'a': 1, 'c': 3}
sorted_d = dict(sorted(d.items()))
print(sorted_d)  # Output: {'a': 1, 'b': 2, 'c': 3}


print("\n""11")
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_by_value)  # Output: {'a': 1, 'b': 2, 'c': 3}



print("\n""12 ")
# Using zip() to Create Dictionaries
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

person = dict(zip(keys, values))
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}







print("\n""13 ")
# Using dict() with map()
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

people = dict(map(lambda name_age: (name_age[0], name_age[1]), zip(names, ages)))
print(people)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

#Step By step
people = dict(map(lambda name_age: (name_age[0], name_age[1]),
                  zip(names, ages)))

zip(names, ages)
Pairs up items by position.
Example: if names = ["Alice", "Bob"] and ages = [25, 30],
zip(...) yields ("Alice", 25), ("Bob", 30) (an iterator of tuples).

map(lambda name_age: (name_age[0], name_age[1]), zip(...))
Applies the lambda to each tuple from zip.
The lambda just returns the same (name, age) tuple it received.
In other words, this map step is redundant—it doesn’t change anything.

dict(...)
Consumes the (name, age) pairs and builds a dictionary:
{"Alice": 25, "Bob": 30}.
If a name appears more than once, the last age wins.
If names and ages have different lengths, zip stops at the shorter one.
✅ Net effect: create a mapping from each name to its age.

    
Simpler (recommended) equivalents
    Shortest:
    people = dict(zip(names, ages))
    
    Or a comprehension:
    people = {n: a for n, a in zip(names, ages)}
    










print("\n""14 ")
#  Using dict.get() Instead of Key Checking
default='default'
# 🚫 Bad:
if 'key' in d:
    value = d['key']
else:
    value = default

# ✅ Better:
value = d.get('key', default)


print("\n""15 ")
#  Use collections.ChainMap for Merging Dictionaries on Demand
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

chain = ChainMap(d1, d2)
print(chain['b'])  # Output: 2 (takes from d1 first)


print("\n""16 ")
# Bonus: Dictionary Memory Optimization
class Person:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alice', 25)
print(p.name, p.age)  # Output: Alice 25
