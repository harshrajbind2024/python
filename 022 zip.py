Pair related data together
Example: You have names and scores stored separately → combine them:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

combined = list(zip(names, scores))
print(combined)
# [('Alice', 85), ('Bob', 90), ('Charlie', 78)]


Loop through multiple lists at once
Instead of managing indices manually:

for name, score in zip(names, scores):
    print(name, "scored", score)


✅ Cleaner and more Pythonic.

Transpose data (rows ↔ columns)
You can "unzip" or rotate data structures:

pairs = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
names, scores = zip(*pairs)
print(names)   # ('Alice', 'Bob', 'Charlie')
print(scores)  # (85, 90, 78)


Parallel iteration with different length lists
By default, zip stops at the shortest list (to avoid missing values).
Example:

a = [1, 2, 3]
b = ['x', 'y']
print(list(zip(a, b)))  
# [(1, 'x'), (2, 'y')]


Combine more than 2 iterables

ids = [101, 102, 103]
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print(list(zip(ids, names, scores)))
# [(101, 'Alice', 85), (102, 'Bob', 90), (103, 'Charlie', 78)]


✅ In short:
We use zip() to make relationships between multiple iterables explicit, making the code shorter, cleaner, and easier to read.

Would you like me to also show you how zip_longest (from itertools) works when lists are of unequal lengths?
