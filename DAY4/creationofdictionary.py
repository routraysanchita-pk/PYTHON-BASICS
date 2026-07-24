info={
        "name":"Sanchita Routray",
        "SIC" : "23BECB12",
        "branch" : "Electronics and Communication Engineering",
        "CGPA" : 9.02,
        "is_adult":True,
        "Projects":["Python AI,ML & DL","Digital Vlsi","Analog Vlsi"],
        "Domain":("AI,ML & DL","DEC","AEC")
        }
print(info)
print(type(info))

#for accessing the keys of dictionary
print (info["name"])
print(info["Projects"])

#dictionary is mutable, to assign or add new
info["age"]=22
print(info)

#for overwriting the new value to the existing key
info["CGPA"]=9.12 
print(info)

#length of the dictionary
print(len(info))
