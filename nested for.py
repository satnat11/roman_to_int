"""
Nested for loop
*
**
***
****
***** (using excel easily  understand row and col)

_______________________

*****
****
***
**
*
________________
ABCDEF
ABCDEF
ABCDEF
ABCDEF



A-Z  ==> 65-90
a-z  ==> 97-122
"""
for i in range(6):
    for j in range(i):
        print("*", end="")
    print("")
print("__________________________")


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")


print("__________________")

for i in range(65,70,1):
    print(chr(i))
print("_____________________")
for i in range (97,102,1):
    print(chr(i))
print("______________________")

for i  in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")