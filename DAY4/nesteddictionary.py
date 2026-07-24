student={
        "name":"Sanchita Routray",
        "SGPA":{
            "1st Sem" : 8.94,
            "2nd Sem" : 9.26,
            "3rd Sem" : 9.22
            },
        "age" : 22
        }

print(student)

#for accessing the nested key:value
print(student["SGPA"]["1st Sem"])

#for adding to the nested key:value
student["SGPA"]["4th Sem"]= 9.13
print(student["SGPA"]["4th Sem"])
print(student)
