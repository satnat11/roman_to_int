# list in python
"""
sequence  type
mutable

a[5]
a={1,2,3,4,5}
a[0]
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("______________________________________")
a=[1,True,'harini',2.6,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][2])

print("______________________________________")
a=[10,20,25,35]
print(a)
a.clear() # clear the entier content
print(a)
a=[10,20,30,40]
b=a.copy()  # copy  the value to one name to other
print(b)
a=[10,20,10,30,40,10,50,60,50]
print(a.count(10))          #no.of times execute 10
print(a.index(20))          #position of the value
print(len(a))
print(min(a))             #miniumum value of a
print(max(a)) #maximum value of a
print(a)
a.pop(1)  # remove element using index
print(a)
a.remove(10) #REMOVEFIRST OCCURENE VALUES
print(a)

print("______________________________________")

names=["sathish"]
print(names)
names.append('nathiya')     #add the values single
names.append("harini")
names.append("kavin")
print(names)
name1=["kumar","sara",'lara']
names.extend(name1)         #group of values add using this
print(names)
names.insert(1,"kumar")     # mention index and add the values
print(names)

print("______________________________________")
print("LIST CONSTRUCTOR  ==> list()")
print(list(range(6)))
print(list("nathiya"))
a=[10,70,20,48,69]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange",'grapes',"apple","lemon"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange",'pineapple',"kiwi","lemon"]
a.sort(key=len)         # based on length
print(a)




