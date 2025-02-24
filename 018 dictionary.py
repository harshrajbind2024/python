# Removes all elements from the dictionary.
d = {'a': 1, 'b': 2}
d.clear()
print(d)  # Output: {}




# Returns a shallow copy of the dictionary.
d = {'a': 1, 'b': 2}
d_copy = d.copy()
print(d_copy)  # Output: {'a': 1, 'b': 2}



# Creates a new dictionary with keys from the iterable and values set to the given default value.
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}


# Returns the value for the key, or the default value if the key is not found.
d = {'a': 1, 'b': 2}
print(d.get('a'))  # Output: 1
print(d.get('z', 'Not Found'))  # Output: Not Found





# If the key exists, returns its value; otherwise, inserts the key with the given default value.
d = {'a': 1}
d.setdefault('b', 2)
print(d)  # Output: {'a': 1, 'b': 2}




# Removes the key and returns its value. If the key is not found, returns the default value.
d = {'a': 1, 'b': 2}
print(d.pop('a'))  # Output: 1
print(d)  # Output: {'b': 2}


# Removes and returns the last key-value pair (insertion order, from Python 3.7+).
d = {'a': 1, 'b': 2}
print(d.popitem())  # Output: ('b', 2)
print(d)  # Output: {'a': 1}

# Returns a view object of all keys in the dictionary.
d = {'a': 1, 'b': 2}
print(list(d.keys()))  # Output: ['a', 'b']


d = {'a': 1, 'b': 2}
print(list(d.values()))  # Output: [1, 2]


# Returns a view object of all key-value pairs as tuples.
d = {'a': 1, 'b': 2}
print(list(d.items()))  # Output: [('a', 1), ('b', 2)]




# Merges another dictionary into the current dictionary.
d = {'a': 1}
d.update({'b': 2, 'c': 3})
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}



# 6. Dictionary Comprehensions
squares = {x: x*x for x in range(5)}
# A concise way to create dictionaries.
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#  Merging Dictionaries (Python 3.9+)
# | (Union Operator)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = d1 | d2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}






# |= (In-place Merge)
d1 |= d2
print(d1)  # Output: {'a': 1, 'b': 3, 'c': 4}





# Using collections.defaultdict
# Provides a default value for missing keys.

from collections import defaultdict
d = defaultdict(int)  # Default value is 0 for missing keys
d['a'] += 1
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})






# Using collections.OrderedDict
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
print(d)  # Output: OrderedDict([('a', 1), ('b', 2)])



# Using collections.Counter for Counting Elements
from collections import Counter
c = Counter("hello")
print(c)  # Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})




# Creates a dictionary by zipping two lists together.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}



d = {'b': 2, 'a': 1, 'c': 3}
sorted_d = dict(sorted(d.items()))
print(sorted_d)  # Output: {'a': 1, 'b': 2, 'c': 3}
