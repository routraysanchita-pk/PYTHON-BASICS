#WRITE A PROGRAM TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENT

List=[1,2,3,4,2,1]
List1=List.copy()
List1.reverse()
if(List1==List):
    print("Yes it is palindrome of elements")
else:
    print("No it is not a palindrome of elements")
