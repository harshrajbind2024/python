def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)




def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120



def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8




def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"




def list_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + list_sum(arr[1:])

print(list_sum([1, 2, 3, 4, 5]))  # Output: 15




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Creating a simple tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

inorder_traversal(root)  # Output: 4 2 1 3






from functools import lru_cache

@lru_cache(maxsize=None)  # Cache results to avoid redundant calls
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Output: 12586269025 (fast computation)






def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

print(factorial_tail_recursive(5))  # Output: 120







print("\n""1 ")
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True



print("\n"" 2")
def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)  # Print solution
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

solve_n_queens(4)
# Output: [1, 3, 0, 2] [2, 0, 3, 1]






# Feature	Recursion	Iteration (Loop)
# Performance	Slower (stack overhead)	Faster (no function calls)
# Memory Usage	High (stack frames)	Low (fixed variables)
# Complexity	Useful for tree/graph problems	Simpler for loops
# Readability	Concise, elegant	Clear for simple loops
# Optimization	Needs memoization	No need





def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)  # Print solution
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

solve_n_queens(4)
# Output: [1, 3, 0, 2] [2, 0, 3, 1]




