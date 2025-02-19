
print("Hello\nWorld")






print(" \n ")
   #vs
print("vs")
print("\n")  


name = "Alice"
age = 25
print(f"Name: {name}\nAge: {age}")



with open("example.txt", "w") as file:
    file.write("First Line\nSecond Line\nThird Line")





lines = ["Line 1", "Line 2", "Line 3"]
result = "\n".join(lines)
print(result)






for i in range(1, 4):
    print("Line {i}\n", end="")  # Avoids extra newlines
       #vs
 
for i in range(1, 4):
    print(f"Line {i}\n", end="")  # Avoids extra newlines
