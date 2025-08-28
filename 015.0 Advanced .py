students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 90},
    {"name": "Charlie", "age": 22, "score": 78}
]

sorted_students = sorted(students, key=lambda x: (x["age"], -x["score"]))  # Sort by age, then descending score
print("\n")
print(sorted_students)
print("\n")

OUTPUT : 
[
    {'name': 'Bob', 'age': 22, 'score': 90},
    {'name': 'Charlie', 'age': 22, 'score': 78},
    {'name': 'Alice', 'age': 25, 'score': 85}
]




fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("\n")

OUTPUT :
0 apple
1 banana
2 cherry








numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print("\n")





from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)
print("\n")

Execute :
Step by step:
reduce(function, iterable) → repeatedly applies the function to the iterable, accumulating a single result.
With lambda x, y: x + y → it adds numbers one by one:
Step 1: 1 + 2 = 3
Step 2: 3 + 3 = 6
Step 3: 6 + 4 = 10
Step 4: 10 + 5 = 15

OUTPUT : 15



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

Step by step:
Original list: [10, 5, 3, 8, 2]
heapq.heapify(nums) reorganizes it into a heap structure internally → ensures the smallest element is always at index 0.
(Heap might look like [2, 5, 3, 8, 10], but order beyond heap property is not guaranteed).
heapq.heappop(nums) → removes and returns the smallest element → 2.






def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(1000000)  # Uses much less memory than a list
print(next(gen))
print("\n")


Step by step:
number_generator(n) is a generator function → it yields values one by one instead of storing them all in memory.
gen = number_generator(1000000) → creates a generator that can produce numbers from 0 to 999999.
next(gen) → gives the first value produced by the generator → 0.




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


#Output
{'Alice': ['Math', 'Science'], 'Bob': ['Science']}






from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter.most_common(1))  # Most common item
print("\n")

# step by step
Counter(data) counts each element’s frequency:
'apple' → 3
'banana' → 2
'orange' → 1
counter.most_common(1) returns the single most common item as a list of (element, count).


#output
[('apple', 3)]






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



#Step by step:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3.
Initial window ([2, 1, 5]) → sum = 8.
Slide the window:
Remove 2, add 1 → sum = 7 → max = 8.
Remove 1, add 3 → sum = 9 → max = 9.
Remove 5, add 2 → sum = 6 → max = 9.
