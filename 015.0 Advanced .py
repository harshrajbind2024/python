students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 90},
    {"name": "Charlie", "age": 22, "score": 78}
]

sorted_students = sorted(students, key=lambda x: (x["age"], -x["score"]))  # Sort by age, then descending score
print("\n")
print(sorted_students)
print("\n")



fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("\n")




names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

combined = list(zip(names, scores))
print(combined)
print("\n")




nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
print("\n")




numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
print("\n")





numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print("\n")





from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
print("\n")





from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # Insert at the beginning
dq.append(4)      # Insert at the end
print(dq)
print("\n")





numbers = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = list(set(numbers))
print(unique_numbers)
print("\n")



import heapq

nums = [10, 5, 3, 8, 2]
heapq.heapify(nums)  # Convert to a heap (min-heap by default)
print(heapq.heappop(nums))  # Remove and return the smallest element
print("\n")






def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(1000000)  # Uses much less memory than a list
print(next(gen))
print("\n")





numbers = [x**2 for x in range(10)]
print(numbers)
print("\n")





logs = ["ERROR: Server down", "INFO: User login", "WARNING: Disk space low"]
sorted_logs = sorted(logs, key=lambda x: x.split(":")[0])  # Sort by log level
print(sorted_logs)
print("\n")







from collections import defaultdict

students = [("Alice", "Math"), ("Bob", "Science"), ("Alice", "Science")]
subjects = defaultdict(list)

for name, subject in students:
    subjects[name].append(subject)

print(dict(subjects))
print("\n")






from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter.most_common(1))  # Most common item
print("\n")






def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
print(max_subarray_sum(nums, 3))
print("\n")
