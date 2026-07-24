info={
        "name":"Sanchita Routray",
        "age" : 22,
        "SGPA" :{
            "1st Sem":8.94,
            "2nd Sem":9.26,
            "3rd Sem":9.22,
            },
        "address":"Cuttack"
        }

print(info)

#key function
print(info.keys())

print(info["SGPA"].keys())    #for nested dictionary

#value function
print(info.values())

#item function
print(info.items())

#get the key function
print(info.get("SGPA"))

#newdictionary function
dict={
        "name":"Pratyush Moharana",
        "Nationality":"Indian",
        "Religion":"Hinduism",
        "State":"Odisha"
        }
info.update(dict)   #name is present in both new and old dictionary the value of the same key will be overwritten as in dictionary duplicate key cant be present

print(info)
info.update({"Mother Tongue":"Odia"})
print(info)
