
print("\n""1 ")
# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")



# To call a function, use the function name followed by parenthesis:
# my_function()

print("\n""2 ")
# Information can be passed into functions as arguments.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters or Arguments?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

print("\n"" 3")
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


print("\n"" 4")
def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil")


print("\n""5 ")
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


#The youngest child is Linus


print("\n""6 ")
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#The youngest child is Linus



print("\n""7 ")
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")


# His last name is Refsnes


print("\n""8 ")
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")   #I am from Sweden
my_function("India")    #I am from India
my_function()           #I am from Norway
my_function("Brazil")   #I am from Brazil






print("\n""9 ")
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)



print("\n""10 ")
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))




print("\n""11 ")
def myfunction():
  pass




print("\n""12 ")
def my_function(x, /):
  print(x)
my_function(3)


#error
# def my_function(x, /):
#   print(x)
# my_function(x = 3)


'

print("\n"" 13")
def my_function(x):
  print(x)

my_function(x = 3)




print("\n""14 ")
def my_function(*, x):
  print(x)

my_function(x = 3)


print("\n"" 14")
def my_function(x):
  print(x)

my_function(3)


print("\n""15 ")
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)




print("\n""16 ")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


print("\n""17 ")
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!



print("\n""18 ")
# *args → Accepts multiple positional arguments
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10



print("\n""19 ")
# **kwargs → Accepts multiple keyword arguments
def user_info(**kwargs):
    return kwargs

print(user_info(name="Alice", age=30))
# Output: {'name': 'Alice', 'age': 30}





print("\n"" 20")
square = lambda x: x ** 2
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 7))  # Output: 10



print("\n""21 ")
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]



print("\n""22 ")
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]


print("\n"" 23")
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24



print("\n""24 ")
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call




print("\n""25 ")
def outer(msg):
    def inner():
        print(msg)
    return inner

func = outer("Hello from closure!")
func()  # Output: Hello from closure!



print("\n""26 ")
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3



print("\n"" 27")
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # Output: 25




print("\n""28 ")
def add(x: int, y: int) -> int:
    return x + y

print(add(3, 4))  # Output: 7





print("\n"" 29")
def calculate_discount(price, discount_rate):
    return price - (price * discount_rate)



print("\n"" 30")
def get_user_age(user):
    return user.get("age", "Unknown")





