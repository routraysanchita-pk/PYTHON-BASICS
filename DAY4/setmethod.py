set1={0,1,2,3,4,5,6,7}
set2={1,2,4,6,9}
print(set1)

#add function
set1.add(8)
print(set1)

#remove function
set1.remove(0)
print(set1)

print(set2)
#pop function
set2.pop()
print(set2)

#union function
print(set1.union(set2))

#intersection function
print(set1.intersection(set2))

#clear function
set1.clear()
print(set1)
print(set2)
