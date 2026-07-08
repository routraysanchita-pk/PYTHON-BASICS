#CONDITIONAL STATEMENT

#FOR IF-ELSE 

age=int(input("Enter your age:"))

if(age>=18):
    print("Can Drive.\nCan Vote")
else:
    print("Not eligible.\nCant drive nor vote")

#FOR IF-ELIF-ELSE
CGPA=float(input("Enter your CGPA:"))
if(CGPA>=9.0):
    print("OUTSTANDING")
elif(CGPA>=8.0 and CGPA<9.0):
    print("EXCELLENT")
elif(CGPA>=7.0 and CGPA<8.0):
    print("VERY GOOD")
elif(CGPA>=6.0 and CGPA<7.0):
    print("GOOD")
else:
    print("IMPROVE")

#NESTING
#people  between age of 18 and 65 can drive
if(age>=18):
    if(age>=65):
        print("CANNOT DRIVE")
    else:
        print("CAN DRIVE")
else:
        print("CANNOT DRIVE")
