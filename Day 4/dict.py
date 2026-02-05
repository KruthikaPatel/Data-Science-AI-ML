# creating dictionary and perform their methods

dict={"id":"105",
      "name":"kruthika",
      "Course":"MCA",
      "sem":"4"}
print(dict)           
#methods
#keys()
print(dict.keys())    
#values()
print(dict.values())   
#items()
print(dict.items())
#get()
print(dict.get("name"))
#update
dict["name"]="Kruthika"
print(dict)
#pop
dict.pop("sem")
print(dict)


for value in dict.values():
    print(value)

    