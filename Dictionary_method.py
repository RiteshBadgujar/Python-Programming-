student={
    "name":"Ritesh badgujar",
    "subject":{
        "math":55,
        "Bio":65,
        "Marathi":60,
        "Eng":72
    },
    "Class":"Mca"
}

contact={ "Mo":123456789}

student.update({"city":"Nahik",})

print(student.keys())   #access all keys

print(student.values()) #Access all Value

pair=list(student.items())
print(pair[0])
print(student.items())      #All item access

print(student.get("city")) #Access using key.

student.update(contact) #update value and new dictionary
print(student)
