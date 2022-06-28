# string and string function
s="nathiya sathish"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.endswith("ya"))
print(s.find("a"))
print(s.find("a",7))
print(s.replace("a",'A'))
a="nathiya162"
print("Is upper:",a.isupper())
print("Is lower:",a.islower())
print("Is alphanumeric:",a.isalnum())
print("Is Alpha:",a.isalpha())
s="she\nis\nmy\ndaughter"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a="welcome to mrs mahal"
print(a.split(" "))
a=" i ,need ,your ,help"
print(a.split(" ,"))
a="   sathish  harini kavin"
print(len(a))
print(len(a.strip()))
print(len(a.lstrip()))
print(len(a.rstrip()))
s='22-06-2022'
print(s.partition('-'))
