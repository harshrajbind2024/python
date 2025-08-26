
##  01

x=22
def printValu():
    x=11
    print("local",x);

print("golble",x);
printValu();

# output 
# golble 22
# local 11




## 02
a=50
def printValu():
   global a
   a=11
   print("inside",a);
#    printValu();   // print multiple time

print("outside",a);
printValu();
print("outside",a);

# # output
# outside 50
# inside 11
# outside 11
