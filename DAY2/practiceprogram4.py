#WRITE A PROGRAM TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))

if(a>=b):
    if(a>=c):
        print(a,"is the greatest")
    else:
        print(c,"is the greatest")
else:
    if(b>=c):
        print(b,"is the greatest")
    else:
        print(c,"is the greatest")

#alternate code
if(a>=b and a>=c):
    print(a,"is the greatest")
elif(b>=c and b>=a):
    print(b,"is the greatest")
else:
    print(c,"is the greatest")
