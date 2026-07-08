#LIST METHODS

l=[2,1,3]
print(l)

#append function
l.append(5)
print("The new list is:",l)

#sort function
l.sort()
print("The ascendingly sorted list is:",l)

#reverse sort function
l.sort(reverse=True)
print("The descendingly sorted list is:",l)

#reverse function
l.reverse()
print("The reversed list is:",l)

#insert element at particualr index function
l.insert(3,4)
print("The new list is:",l)

#remove function
l.remove(2)
print("After removing:",l)

#pop function
l.pop(2)
print("The final list:",l)
