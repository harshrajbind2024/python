#Strings
text = "Hello, Python!"
print(text)
print("Python" in text)   
print("World" in text)    
print("\n") 

#list
fruits = ["apple", "banana", "cherry"]
print(fruits)
print("apple" in fruits)  
print("grape" in fruits)   
print("\n") 

#string
text = "Python is fun"
print(text)
print("Java" not in text)   
print("Python" not in text)  
print("\n") 

#list
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(10 not in numbers)  
print(3 not in numbers)   
print("\n") 

# tuple
colors = ("red", "green", "blue")
print(colors)
print("green" in colors)   
print("yellow" in colors) 
print("\n") 




# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)
print("name" in person)   
print("Alice" in person)   
print("age" not in person)   
print("\n") 


#set
numbers = {10, 20, 30, 40}
print(numbers)
print(20 in numbers)  
print(50 in numbers)  
print("\n") 

valid_users = ["admin", "guest", "user"]
username = input("Enter username: ")

if username in valid_users:
    print("Access granted")
else:
    print("Access denied")
print("\n") 