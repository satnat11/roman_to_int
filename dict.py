user={
    "name":"nathiya",
     "age":35,
    "ismarried":True
}
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))      #get built in function use
print(user.values())        #display only for values
print(user.items())         #display both key and values

#using for loop

for x in user:
    print(x," ",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

if "age" in user:
    print("present")

#changing values

user.update({"gender":"female"})
print(user)
user["age"]=36
print(user)
user.pop("age")
print((user))
user.clear()
print(user)

print("**************MULTIPlE DICTIONARIES ADD   **********")

users={
"user1":{
    "name":"nathiya",
     "age":35,
    "ismarried":True
},
"user2":{
    "name":"sathiya",
     "age":26,
    "ismarried":False
},
"user3":{
    "name":"nithiya",
     "age":50,
    "ismarried":True
},

}
print(users)