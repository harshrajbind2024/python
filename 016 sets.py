# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

# Creating an empty set (Must use set(), NOT {})
empty_set = set()
print(type(empty_set))  # <class 'set'>


numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}


numbers.update([5, 6, 7])
print(numbers)  # {1, 2, 3, 4, 5, 6, 7}


numbers.remove(3)
print(numbers)  # {1, 2, 4, 5, 6, 7}



numbers.discard(10)  # No error
print(numbers)  # {1, 2, 4, 5, 6, 7}



numbers = {1, 2, 4, 5, 6, 7}
numbers.discard(5)
print(numbers) # {1, 2, 4, 6, 7}


popped_value = numbers.pop()
print(popped_value)  # Random element
print(numbers)




numbers.clear()
print(numbers)  # set()



A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print(C)  # {1, 2, 3, 4, 5}



C = A.intersection(B)
print(C)  # {3}
  

C = A.difference(B)
print(C)  # {1, 2}


print(A | B)  # Union → {1, 2, 3, 4, 5}
print(A & B)  # Intersection → {3}
print(A - B)  # Difference → {1, 2}


# Checking Relationships Between Sets

A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))  # True



print(B.issuperset(A))  # True



X = {1, 2}
Y = {3, 4}
print(X.isdisjoint(Y))  # True




#  Set Comprehension
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # {1, 4, 9, 16, 25}



A = frozenset([1, 2, 3, 4])
# A.add(5)  # ❌ Error: Cannot modify frozen set
print(A)  # frozenset({1, 2, 3, 4})



# Real-World Examples
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]




students_A = {"Alice", "Bob", "Charlie"}
students_B = {"Charlie", "David"}
common_students = students_A & students_B
print(common_students)  # {"Charlie"}


names = {"Alice", "Bob", "Charlie"}
print("Bob" in names)  # ✅ Fast



# Category	Functions
# Adding Elements	add(), update()
# Removing Elements	remove(), discard(), pop(), clear()
# Set Operations	union(), intersection(), difference()
# Relationships	issubset(), issuperset(), isdisjoint()
# Other	frozenset()




import time
# Large dataset
items = list(range(1000000))   # [0, 1, 2, 3, 4, 5, ..., 999999]
items_set = set(items)         #{0, 1, 2, 3, 4, 5, ..., 999999}


# Checking membership in a list
start = time.time()
print(999999 in items)  # ✅ Slow           #True
print("List time:", time.time() - start)   #True


# Checking membership in a set
start = time.time()
print(999999 in items_set)  # ✅ Very Fast
print("Set time:", time.time() - start)




emails = ["a@gmail.com", "b@yahoo.com", "a@gmail.com", "c@gmail.com"]
unique_emails = list(set(emails))
print(unique_emails)  # ['a@gmail.com', 'b@yahoo.com', 'c@gmail.com']



dataset1 = {1, 2, 3, 4, 5, 6, 7}
dataset2 = {5, 6, 7, 8, 9}
common_values = dataset1 & dataset2
print(common_values)  # {5, 6, 7}



text = "Python is awesome. Python is powerful."
unique_words = set(text.lower().split())
print(unique_words)  # {'python', 'is', 'awesome.', 'powerful.'}




user_tags = {"python", "machine learning", "ai"}
search_tags = {"data science", "ai", "deep learning"}

matching_tags = user_tags & search_tags
print(matching_tags)  # {'ai'}




permissions = frozenset(["read", "write"])
# permissions.add("delete")  # ❌ Error: Cannot modify frozenset




large_set = set(range(1000000))
precomputed_intersection = large_set & {999999}
print(precomputed_intersection) #{999999}

big_list = list(range(1000000))  
big_set = set(big_list)  

# Bad approach
999999 in big_list  # ❌ Slow (O(n))

# Optimized approach
999999 in big_set  # ✅ Fast (O(1))
