my_tuple = (1, 2, 3, 4)
print(my_tuple)  # (1, 2, 3, 4)


my_tuple = 1, 2, 3
print(my_tuple)  # (1, 2, 3)


single = (5,)  
print(type(single))  # <class 'tuple'>

empty = ()
print(type(empty))  # <class 'tuple'>




tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)  # (1, 2, 3)




numbers = (10, 20, 30, 40)
print(numbers[0])  # 10
print(numbers[-1])  # 40





print(numbers[1:3])  # (20, 30)
print(numbers[:2])  # (10, 20)
print(numbers[::-1])  # Reverse tuple: (40, 30, 20, 10)





t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2  
print(result)  # (1, 2, 3, 4, 5)






repeated = t1 * 3  
print(repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)





nums = (1, 2, 2, 3, 4, 2)
print(nums.count(2))  # 3




print(nums.index(3))  # 3



# Speed Comparison (Tuple vs List)
import time

# Creating a list and tuple
my_list = list(range(1000000))
my_tuple = tuple(my_list)

# Timing list access
start = time.time()
for _ in range(1000000):
    _ = my_list[500000]
print("List access time:", time.time() - start)

# Timing tuple access
start = time.time()
for _ in range(1000000):
    _ = my_tuple[500000]
print("Tuple access time:", time.time() - start)





#  Packing a Tuple
data = "Alice", 25, "Engineer"
print(data)  # ('Alice', 25, 'Engineer')



name, age, profession = data
print(name)  # Alice
print(age)   # 25
print(profession)  # Engineer




first, *middle, last = (1, 2, 3, 4, 5)
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5




def get_user():
    return "Alice", 25

name, age = get_user()
print(name, age)  # Alice 25




coordinates = {(10, 20): "Point A", (30, 40): "Point B"}
print(coordinates[(10, 20)])  # Point A






students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]





# Feature	Tuple ✅	List ✅
# Mutable (Changeable)?	❌ No	✅ Yes
# Faster in Iterations?	✅ Yes	❌ No
# Memory Efficient?	✅ Yes	❌ No
# Indexing & Slicing?	✅ Yes	✅ Yes
# Used as Dictionary Keys?	✅ Yes	❌ No
# Stores Fixed Data?	✅ Yes	❌ No
