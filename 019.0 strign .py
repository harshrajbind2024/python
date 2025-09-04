print("\n""1 ")
s = " hello world "
print(s.upper())         # HELLO WORLD
print(s.lower())         # hello world
print(s.title())         # Hello World
print(s.capitalize())    # Hello world
print(s.swapcase())      # HELLO WORLD -> hELLO WORLD
print(s.replace("world", "Python"))  # hello Python
print(s.strip())         # Removes spaces from start & end



print("\n""2 ")
# Useful for formatting numbers as fixed-width strings.
num = "42"
print(num.zfill(5))       # Output: '00042'

#STEP BY STEP
Here’s what happens step by step:
num = "42"
num is a string, not a number. Its length is 2.
num.zfill(5)
zfill(width) pads the left side of the string with '0' until the string’s total length is width.
Needed zeros = 5 - len("42") = 5 - 2 = 3.
Result of the call
"000" + "42" → "00042".
print(num.zfill(5))

#OTHER 
"-42".zfill(5) → "-0042"
"+42".zfill(5) → "+0042"




print("\n""3 ")
# str.startswith() and str.endswith() → Check Prefix/Suffix
filename = "data.csv"

print(filename.startswith("data"))     # Output: True
print(filename.endswith(".csv"))       # Output: True





print("\n"" 4")
# str.partition() and str.rpartition() → Split String Into Three Parts
s = "hello-world-python"

print(s.partition("-"))             # ('hello', '-', 'world-python')
print(s.rpartition("-"))            # ('hello-world', '-', 'python')



print("\n""4 ")
# multiple character replacements:
table = str.maketrans("aeiou", "12345")  # Create a translation table
s = "hello world"
print(s.translate(table))  # h2ll4 w4rld


print("\n""5 ")
# str.casefold() → Best for Case-Insensitive Comparisons
# More aggressive than .lower() (handles Unicode cases).
s1 = "Straße"
s2 = "STRASSE"
print(s1.casefold() == s2.casefold())  # Output: True

#Step by Step
✅ Explanation:
s1 = "Straße" (German sharp S).
s2 = "STRASSE".
Using .lower() would not match properly in some cases, but .casefold() is designed for case-insensitive and Unicode-aware comparison.
"straße".casefold() → "strasse"
"STRASSE".casefold() → "strasse"




print("\n""6 ")
# re Module → Regular Expressions for Pattern Matching
# Python's re module allows powerful string pattern searches.
import re
text = "My phone number is 123-456-7890"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(match.group())  # Output: 123-456-7890


#step by step
\d{3} → matches exactly 3 digits.
- → matches a literal dash.
\d{4} → matches exactly 4 digits.
So the regex \d{3}-\d{3}-\d{4} matches a phone number pattern like 123-456-7890.
re.search() finds the first match, and .group() returns the matched string.






print("\n""7 ")
# format() and f-strings → Advanced String Formatting
# Python f-strings (f"") provide clean, efficient formatting.
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 30 years old.





print("\n""8 ")
# Joining and Splitting Strings Efficiently
# Efficiently join elements of a list into a string:
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome








print("\n"" 9")
text = "Hello 🌍"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print(encoded)  # Output: b'Hello \xf0\x9f\x8c\x8d'
print(decoded)  # Output: Hello 🌍

#step by staep
    encode() converts a Python string (str, Unicode) into bytes using a given encoding (e.g., "utf-8").
    decode() converts bytes back into a Python string, interpreting them with the same encoding.
    They are opposites: str → bytes with encode(), and bytes → str with decode(). ✅



print("\n"" 10")
import string
s = "Hello, world!!!"
cleaned = s.translate(str.maketrans("", "", string.punctuation))
print(cleaned)  # Output: Hello world




print("\n""11 ")
#  Using str.join() Instead of + for Concatenation
s = ""
for word in ["hello", "world"]:
    s += word + " "  # Slow due to repeated memory allocation


s = " ".join(["hello", "world"])  


print("\n""12 ")
# Instead of multiple .replace() calls:
import re

s = "hello world"
s = re.sub(r"[aeiou]", "*", s)  # Replace vowels with '*'
print(s)  # h*ll* w*rld




print("\n""13 ")
import textwrap

text = "Python is a powerful programming language that is easy to learn."
wrapped = textwrap.fill(text, width=20)

print(wrapped)
# Python is a powerful
# programming language
# that is easy to learn.




print("\n""14 ")
from difflib import SequenceMatcher

s1 = "Hello world"
s2 = "Hello Python"

similarity = SequenceMatcher(None, s1, s2).ratio()
print(similarity)  # Output: 0.769





print("\n"" 16")
s = "Python"

print(s.ljust(10, "-"))  # Python----
print(s.rjust(10, "-"))  # ----Python
print(s.center(10, "-"))  # --Python--


print("\n""17 ")
# Check if a String is a Valid Variable Name
print("my_var".isidentifier())  # True
print("123var".isidentifier())  # False


print("\n""18 ")
# Convert Tabs to Spaces
s = "Hello\tWorld"
print(s.expandtabs(8))  # Hello   World





# Count Substring Occurrences Efficiently

print("\n""19 ")
s = "banana banana banana"
print(s.count("banana"))  # 3





# Different ways to handle encoding errors:
print("\n""20 ")
text = "Café"
encoded = text.encode("ascii", errors="ignore")  # Ignore unsupported characters
print(encoded)  # Output: b'Caf'




#  Using map() to Apply a Function to Each Character

print("\n"" 21")
s = "hello"
mapped = "".join(map(lambda c: c.upper(), s))
print(mapped)  # HELLO



print("\n""22 ")
#  Using filter() to Remove Unwanted Characters
s = "hello 123 world"
filtered = "".join(filter(str.isalpha, s))
print(filtered)  # helloworld



print("\n""23 ")
# Using functools.reduce() for Custom String Manipulations
from functools import reduce

words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Python is awesome



print("\n"" 24")
# Using re.finditer() for Efficient Pattern Matching
import re

s = "apple, banana, cherry"
matches = re.finditer(r"\b\w{6}\b", s)  # Words with exactly 6 letters

for match in matches:
    print(match.group())  # banana, cherry



print("\n""25 ")
# Using str.format_map() for Dynamic String Formatting
data = {"name": "Alice", "age": 30}
s = "{name} is {age} years old".format_map(data)
print(s)  # Alice is 30 years old



print("\n""27 ")
#  Faster String Searching with str.find() vs. in Operator
s = "hello world"

print(s.find("world"))  # 6 (index)
print("world" in s)  # True (boolean check)





print("\n""28 ")
# Using itertools.groupby() for Grouping Consecutive Characters
from itertools import groupby

s = "aaabbccccdaa"
grouped = ["".join(g) for _, g in groupby(s)]
print(grouped)  # ['aaa', 'bb', 'cccc', 'd', 'aa']






print("\n""29 ")
# Reversing a String in Python
s = "Python"
print(s[::-1])  # nohtyP



print("\n""30 ")
#  Removing Duplicate Characters from a String
s = "banana"
unique_chars = "".join(dict.fromkeys(s))  # 'ban'
print(unique_chars)



print("\n""31 ")
# Finding the Most Common Character in a String/
from collections import Counter

s = "banana"
most_common = Counter(s).most_common(1)[0][0]
print(most_common)  # 'a'



    
