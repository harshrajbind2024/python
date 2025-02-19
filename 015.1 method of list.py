numbers = [1, 2, 3]
numbers.append(4)  
print(numbers)  # [1, 2, 3, 4]



numbers.insert(1, 10)  
print(numbers)  # [1, 10, 2, 3, 4]


more_numbers = [5, 6, 7]
numbers.extend(more_numbers)  
print(numbers)  # [1, 10, 2, 3, 4, 5, 6, 7]


numbers.remove(10)  
print(numbers)  # [1, 2, 3, 4, 5, 6, 7]


last = numbers.pop()  
print(last)  # 7
print(numbers)  # [1, 2, 3, 4, 5, 6]




numbers.clear()
print(numbers)  # []





#  Searching & Indexing Functions#


colors = ['red', 'blue', 'green', 'blue']
print(colors.index('blue'))  # 1



print(colors.count('blue'))  # 2



# Sorting & Reversing

nums = [5, 3, 8, 2]
nums.sort()  
print(nums)  # [2, 3, 5, 8]



nums = [5, 3, 8, 2]
sorted_nums = sorted(nums)  
print(sorted_nums)  # [2, 3, 5, 8]
print(nums)  # [5, 3, 8, 2]




nums.reverse()  
print(nums)  # [8, 5, 3, 2]





original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(original)  # [1, 2, 3]
print(copied)  # [1, 2, 3, 4]




#  Mathematical Operations

nums = [10, 20, 30, 40]
print(len(nums))  # 4

print(sum(nums))  # 100


print(max(nums))  # 40


print(min(nums))  # 10


# Functional Programming


nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]



even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(even_numbers)  # [2, 4]




from functools import reduce

sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # 10




from functools import reduce

sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # 10





# Advanced Data Structures
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # Insert at the beginning
dq.append(4)      # Insert at the end
print(dq)  # deque([0, 1, 2, 3, 4])



import heapq

heap = [10, 5, 3, 8, 2]
heapq.heapify(heap)  
print(heap)  # [2, 5, 3, 8, 10] (min-heap structure)




#  Real-World Applications

logs = ["ERROR: Server down", "INFO: User login", "WARNING: Disk space low"]
sorted_logs = sorted(logs, key=lambda x: x.split(":")[0])  # Sort by log level
print(sorted_logs)


from collections import defaultdict

students = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Science")]
subjects = defaultdict(list)

for name, subject in students:
    subjects[name].append(subject)

print(dict(subjects))  
# {'Alice': ['Math', 'Science'], 'Bob': ['Science']}



from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter.most_common(1))  # [('apple', 3)]










# Basic Operations	append(), insert(), extend(), remove(), pop(), clear()
# Searching & Indexing	index(), count()
# Sorting & Reversing	sort(), sorted(), reverse()
# Copying & Cloning	copy()
# Math Operations	len(), sum(), max(), min()
# Functional Programming	map(), filter(), reduce()
# Advanced Structures	deque(), heapify()