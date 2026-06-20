#Dictionary : Dictionary in python are key value pair where each key maps to a value 1. they are unordered,mutable and used for storing and accessing data efficiently
# my_dict={
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3"
# }
contact={
    "name":"tanu",
    "age":"22",
    "phone":"9548771891",
    "email":"tanuchauhan18004@gmail.com"
}
#accessing the item inside dictionary
print(contact["phone"]) 

#modifing the value inside the dictionary
contact["phone"]="9412823958"

#adding and 
contact["address"]="moh. kila"
print(contact)

#removing items
del contact["email"]
print(contact)

#looping through dictionary
for key,value in contact.items():
    print(key,value)
    
if "email" in contact:
    print("found")
else:
    print("not found")