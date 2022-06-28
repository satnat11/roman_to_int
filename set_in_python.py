"""
unordered(we can't change orderwise)
{}
"""

names={'sathish','harini','kavin'}
print(names)
print(type(names))

#Access values using for loop
for name in names:
    print(name)

#Adding new element
names.add('nathiya')
print(names)

#Update another set of data
a={'john','raj','kumar'}
names.update(a)
print(names)

#remove data
names.remove('raj')
print(names)
#discard
names.discard('john')
print(names)

names.pop()
print(names)

names.clear()
print(names)

del names
print(names)


names={'sathish','harini','sara','kavin','raj','banu','sara'}
print(names)


a={1,2,3,4,5}
b={'a','b','c','d','e'}
c=a.union(b)    #join the both values
print(c)
a.update(b)     #the same value but hereusing update
print(c)

print("***********************************")
a={3,4,5}
b={3,4,5}

c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)


c=a.isdisjoint(b)
print(c)
c=a.issubset(b)     #same value of both
print(c)
c=a.issuperset(b)
print(c)
