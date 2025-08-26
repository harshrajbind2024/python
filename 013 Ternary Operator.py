age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)





a, b = 5, 10

# 1. Standard ternary operator
min_val1 = a if a < b else b

# 2. Tuple indexing
min_val2 = (b, a)[a < b]  

# 3. Dictionary mapping
min_val3 = {True: a, False: b}[a < b]

# 4. Logical and/or
min_val4 = (a < b and a) or b  

print("Standard ternary  :", min_val1)
print("Tuple indexing    :", min_val2)
print("Dictionary method :", min_val3)
print("Logical and/or    :", min_val4)


✅ Output:
Standard ternary  : 5
Tuple indexing    : 5
Dictionary method : 5
Logical and/or    : 5
