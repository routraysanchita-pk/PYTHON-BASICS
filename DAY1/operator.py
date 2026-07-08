
a=1000
b=500


#ARITHMETIC OPERATORS
diff=a-b; #substraction 
mul=a*b; #multiplication
div=a/b; #division
sum=a+b; #addition
remainder=a%b; #find remainder
expo=a**2
print("The sum of 1000 & 500 is:", sum);
print("The difference of 1000 & 500 is:", diff);
print("The product of 1000 & 500 is:", mul);
print("The quotient of 1000 & 500 is:", div);
print("The remainder of 1000 & 500 is:" , remainder);
print("The value of 1000 to the power 2:", expo);


#RELATIONAL OPERATORS
print(a > b) #greater than
print(a >= b) #greater than equal to
print(a < b) #lesser than 
print(a <= b) #lesser than equal to
print(a == b) #equal to
print(a != b) #not equal to


#ASSIGNMENT OPERATOR
num = 10
num += 10 #num = num + 10 #ans=20
num -= 5 #num = num - 5 #ans-15
num *= 2 #num = num * 2 #ans=30
num /= 5 #num = num / 5 #ans=6
num **= 2 #num = num ** 2 #ans=36
print("Now the number is:" , num)


#LOGICAL OPERATORS
val1=True
val2=False
print("NOT OPERATOR:", not val1) #inverted output
print("AND OPERATOR:" , val1 and val2) #gives true when both the value is true or else false
print("OR OPERATOR:" , val1 or val2) #gives true even if one value is true
