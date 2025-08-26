my_list = [10, 20, 30, 40, 50]
print(my_list)
print("\n\n")

print(my_list[0])    # First element
print(my_list[-1])   # Last element
print(my_list[1:4])  # Slice from index 1 to 3
print("\n\n")


my_list[1] = 25  # Change value at index 1
print(my_list)
print("\n\n")


my_list.append(60)      # Add at the end
my_list.insert(2, 35)   # Insert at index 2
print(my_list)
print("\n\n")


my_list.remove(30)  # Remove first occurrence of 30
print(my_list)
print("\n\n")




popped_value = my_list.pop()  # Remove and return last element
print(popped_value, my_list)
print("\n\n")



for item in my_list:
    print(item)
print("\n\n")


my_list.sort()        # Sort in ascending order
print(my_list)
print("\n\n")






my_list.reverse()     # Reverse the list
print(my_list)
print("\n\n")






squared = [x**2 for x in my_list]
print(squared)
print("\n\n")





numbers = [10, 20, 30, 20, 40, 10, 50]
squared_list = list(map(lambda x: x ** 2, numbers))
print(squared_list)
print("\n\n")

#OUTPUT
[100, 400, 900, 400, 1600, 100, 2500]

other way
#1
import numpy as np
numbers = [10, 20, 30, 20, 40, 10, 50]
squared_list = np.square(numbers).tolist()

#2
squared_list = list(map(pow, numbers, [2] * len(numbers)))

#3
squared_list = []
for x in numbers:
    squared_list.append(x ** 2)

#4
squared_list = [x ** 2 for x in numbers]





list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)
print("\n\n")

#OutPut
[1, 2, 3, 4, 5, 6]



list1.extend(list2)
print(list1)
print("\n\n")

#OUTPUT
[1, 2, 3, 4, 5, 6]






names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
paired_list = list(zip(names, scores))
print(paired_list)
print("\n\n")


#OUTPUT
[("Alice", 85), ("Bob", 90), ("Charlie", 78)]

#OTHER
#01
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78, 55
paired_list = list(zip(names, scores))
print(paired_list)
print("\n\n")

#note:
The extra 55 in scores is ignored, because names has only 3 elements.

#Execution:: paired_list = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
#OUTPUT
[('Alice', 85), ('Bob', 90), ('Charlie', 78)]

#02
paired_list = [(names[i], scores[i]) for i in range(len(names))]
print(paired_list)

#03
paired_dict = dict(zip(names, scores))
print(paired_dict)

#04
paired_list = [(names[i], score) for i, score in enumerate(scores)]
print(paired_list)





nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
print("\n\n")





numbers = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = list(set(numbers))
print(unique_numbers)
print("\n\n")






students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by age
print(sorted_students)
print("\n\n")








words = ["apple", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=len)  # Sort by word length
print(sorted_words)
print("\n\n")











nums = [5, 3, 8, 1, 9]
sorted_nums = sorted(nums, reverse=True)  # Sort in descending order
print(sorted_nums)
print("\n\n")








my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]  # Reverse using slicing
print(reversed_list)
print("\n\n")







nums = [10, 20, 30, 40, 50, 60]
every_second = nums[::2]
print(every_second)
print("\n\n")
clear_list=nums.clear();
print(clear_list)





original = [1, 2, 3]
copy_list = original[:]
copy_list.append(4)
print(original)  # Unchanged
print(copy_list)  # Modified
print("\n\n")






list1=[1,2,34,5]
li2=list1
print('li2  ',li2)
print("\n")
li3=list1.copy()
print(li3)
print("\n")






from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # Insert at the beginning
dq.append(4)      # Insert at the end
print(dq)
print("\n\n")








from itertools import permutations, combinations

items = [1, 2, 3]
print(list(permutations(items, 2)))  # All 2-item orderings
print(list(combinations(items, 2)))  # All 2-item groups
print("\n\n")








import heapq

nums = [10, 5, 3, 8, 2]
heapq.heapify(nums)  # Convert to a heap (min-heap by default)
print(heapq.heappop(nums))  # Remove and return the smallest element
print("\n\n")



