#   tuple in python
#   immutable
#   surrounded by round brackets(1,2.3,True)

a=(1,3.5,"harini",True)
print(a)
print(type(a))
print(a[1])
print(a[-1])            #reverse value(last value print)
print(a[0:3])
b=list(a)         #add any values in tuple convert list  and using append() add the values after that   convert tuple
print(b)
b.append("kavin")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

print("$$$$$$$$ using for loop and if condition  $$$$$$$$$$$$$$$")
for i in a:
      print(i)


if "kavin" in a:
      print("kavin is found")
else:
      print("not found")
print(len(a))


a=(1)             # it will take int
print((type(a)))
a=(1,)            # , it will take tuple
print((type(a)))
del a             # delete entire data

a=(1,2,3,4,5)
b=(6,3,8,9,10)
c=a+b
print(c)
print(c.count(3))       # 3 no of times execte


a=(1,2,3,4,5)
b=(6,3,8,9,10)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[1][3])          #its looking like matrix


x=('hai',)*5            #we used comma then only it will take tuple
print(x)


a=(1,8,3,5)
print(min(a))
print(max(a))


