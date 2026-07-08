#USER INPUT
name=input("Enter your name :")
print("WELCOME" , name)

age=int(input("Enter your age :"))
"""
typecasting is necessary 
as the value we enter in input is by default considered as string
"""
print("So your age is" , age)

CGPA=input("Enter your CGPA:")

print(type(name))
print(type(age))
print(type(CGPA))
