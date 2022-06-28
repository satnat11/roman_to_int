# nested if statement in python
"""
 3 marks as input
 calculate tot,avg,result
 if pass
    grade
    90-100      A
    80-89       B
    70-79       c
    else        d
"""
m1=int(input("enter the mark1: "))
m2=int(input("enter the mark2: "))
m3=int(input("enter the mark3: "))
Total=m1+m2+m3
Average=Total/3.0
print("Total: ",Total)
print("Average:",Average)
if m1>=35 and m2>=35 and m3>=35:
    print('Result: Pass')
    if  Average >=90 and Average<=100:
        print("Grade: A")
    elif Average >=80 and Average<=89:
        print("Grade: B")
    elif Average >=70 and Average <=79:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: Fail")
    print("Grade:  No Grade")
