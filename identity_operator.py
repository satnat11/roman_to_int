"""
is
is not
"""
a=[1,2,3]
b=[1,2,3]
c=a
print(c)
print(a is c)       #only compare object not a values
print(id(a))
print(id(b))
print(id(c))
print(a is b)       #id value is different so false
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(a==b)         #compare values only
print(a is not b)   #compare identity
print(a is not c)
print(a!=b)     # here compare values