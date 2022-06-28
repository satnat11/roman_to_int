def welcome():
    print("welcome to mrs mahal")

welcome()
welcome()
# no return type without argument function in python
"""
def add():
    a=int(input("enter tha a value: "))
    b=int(input("enter the b value: "))
    c=a+b
    print("Total:",c)

add()
"""
# no return type with argument function in python
"""
def sub(a,b):
    c=a-b
    print("Difference:",c)

sub(20,7)
"""
#  return type without argument function in python
"""
def mul():
    a = int(input("enter tha a value: "))
    b = int(input("enter the b value: "))
    c=a*b
    return(c)


print("Multiplication is :",mul())
"""

#  return type with argument function in python

"""
def div(a,b):
    c=a/b
    return (c)
x=div(20,2)
print("division:",x)
"""
# arbitrary arguments function in python(*)
"""
def class_10(*students):
    print(students)
    for user in students:
        print(user)

class_10("sara","sam","kavin","harini","kumar")
"""

# keyword arguments funtion in python
"""
def message(name,age):
    print(name,"age is",age)

message(23,"sam")   #change the argument value
message(age=23,name='sam')  #keyword use and get the proper data
"""
# arbitrary keyword arguments in python
"""
def bioData(**data):
    print(data)

bioData(name="ram",age=27,gender="male")
"""

# Default parameter function in python

"""
def user(name,city="salem"):
    print(name,"is from ",city)

user("sam","trichy")
user("ram")     #default value assigned
"""
#passing a list as an argument in function in python
"""
def total(marks):
    return sum(marks)
print("Total is: ",total([25,56,32,78,45]))

"""
# recursive function
# 1*2*3*4*5=120
"""
def factorial(x):
    if x==1:
        return  1
    else:
        return (x*factorial(x-1))

print("Factorial is: ",factorial(5))
"""
"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1=120
"""


c=lambda a:a+50
print(c(10))

c=lambda a,b:a*b
print(c(2,6))