#STRING FUNCTIONS

str="my name is Sanchita Routray"

print("length the string is:",len(str))  #length function

#endswith function
print("Is the string ends with 'y':",str.endswith("y"))
print("Is the string ends with 'a':",str.endswith("a"))

#capitalize function
print("Your sentence:",str.capitalize())

#to capitallize the string and store it
str1=str.capitalize() 
print(str1)

#replace function
print("New name:",str.replace("s","f"))
print("New name:",str.replace("Sanchita","Ankita"))

#find function
print(str.find("Routray"))
print(str.find("o"))

#count function
print("the letter 'a' is repeated for" ,str.count("a"),"times")
print("the word 'Routray' is repeated for" , str.count("Routray"),"times")
