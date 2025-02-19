a = 5   # 0101
b = 3   #  0011



result = a & b 
 # 0001 (1 in decimal)
print(' a & b=',result)  
# Output: 1



result = a | b
print(' a | b=',result) 




result = a ^ b 
print(' a ^ b=',result)



result = ~a # 0101
print(' ~a=',result)



result = a << 1   # 0101
print(' a << 1 =',result)



result = a >> 1  # 0101
print(' a >> 1=',result)




num = 7
if num & 1:
    print("Odd")
else:
    print("Even")
