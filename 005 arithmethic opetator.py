
# #01
a,b=10,20;
c=a+b;
print("sum of",a, "and",b,"=",c);

print("multiplication of",a, "and",b,"=",a*b);

print("a power of b=",a**b, "\n","b power of a=",b**a);





#02
def arithmetic_operations(arr, num):
    results = {
        "Addition": [x + num for x in arr],
        "Subtraction": [x - num for x in arr],
        "Multiplication": [x * num for x in arr],
        "Division": [x / num for x in arr],
        "Floor Division": [x // num for x in arr],
        "Modulus": [x % num for x in arr],
        "Exponentiation": [x ** num for x in arr]
    }
    return results

numbers = [10, 20, 30, 40, 50]

result = arithmetic_operations(numbers, 5)

for operation, values in result.items():
    print(f"{operation}: {values}")



#output
# Addition: [15, 25, 35, 45, 55]
# Subtraction: [5, 15, 25, 35, 45]
# Multiplication: [50, 100, 150, 200, 250]
# Division: [2.0, 4.0, 6.0, 8.0, 10.0]
# Floor Division: [2, 4, 6, 8, 10]
# Modulus: [0, 0, 0, 0, 0]
# Exponentiation: [100000, 3200000, 24300000, 102400000, 312500000]
