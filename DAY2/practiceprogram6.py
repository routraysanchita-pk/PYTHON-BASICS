# WRITE A PROGRAM TO FIND THE GREATEST AMONG 4 NUMBERS

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("Greatest number is:", num1)
elif (num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("Greatest number is:", num2)
elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
    print("Greatest number is:", num3)
else:
    print("Greatest number is:", num4)
