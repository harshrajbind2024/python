print("\n""1 ")
txt = "The best things in life are free!"
print("free" in txt) 



#True


print("\n""2 ")
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") 




#Yes, 'free' is present.






print("\n""3 ")
txt = "The best things in life are free!"
print("expensive" not in txt)  



#True




print("\n""4")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



print("\n""5 ")
# Slicing
b = "Hello, World!"
print(b[:5]) 


#Hello



print("\n""6 ")
b = "Hello, World!"
print(b[2:]) 


#llo, World!



print("\n""7 ")
b = "Hello, World!"
print(b[-5:-2])


#orl


print("\n""8 ")
# Modify Strings
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']


#
HELLO, WORLD!
hello, world!
Hello, World!
Jello, World!
['Hello', ' World!']




print("\n""9 ")
# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)



#HelloWorld


print("\n""10 ")
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#Hello World


print("\n"" 11")
# Python - Format - Strings
age = 36
txt = "My name is John, I am " + age
print(txt)



#
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    txt = "My name is John, I am " + age
TypeError: can only concatenate str (not "int") to str



print("\n""12 ")
age = 36
txt = f"My name is John, I am {age}"
print(txt)


#My name is John, I am 36
 

print("\n""13 ")
price = 59
txt = f"The price is {price} dollars"
print(txt)




print("\n""14 ")
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#The price is 59.00 dollars



print("\n"" 15")
txt = f"The price is {20 * 59} dollars"
print(txt)



print("\n"" 16")
# Escape Character
txt = "We are the so-called \"Vikings\" from the north."

# Code	Result	 
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value



# String Methods
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



print("\n""17 ")
# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)


print("\n"" 18")
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")





print("\n"" 19")
print(bool("Hello"))
print(bool(15))


#
True
True



print("\n"" 20")
x = "Hello"
y = 15
print(bool(x))
print(bool(y))


#
True
True



print("\n""21 ")
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



# The following will return False:
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})


print("\n""22 ")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))




print("\n""23 ")
def myFunction() :
  return True

print(myFunction())




print("\n""24 ")
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


print("\n""25 ")
x = 200
print(isinstance(x, int))


# True




