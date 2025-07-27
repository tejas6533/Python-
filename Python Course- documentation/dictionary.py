"""
info = {
    "name": "Tejastagde",
    "age": 25,
    "city": "Pune",
    "hobbies": ["reading", "coding", "gaming"],
    "is_adult": False
}
print(info["hobbies"])
print(info["is_adult"])

info ["city"] = "nagpur"
print(info)

"""
#Nested dictionary
"""
collage = {
    "name": "Smit Surkar",
    "age" : 20,
     "subjects":{
         "phy": 75,
            "chem": 80,
            "maths": 50
     },

     }
print(collage["subjects"] ["phy"])

"""

# methods of dictionary

"""
collage = {
    "name": "Smit Surkar",
    "age" : 20,
     "subjects":{
         "phy": 75,
            "chem": 80,
            "maths": 50
     },

     }
collage.update({"age":21 , "city": "nagpur"})
print("Updated age:", collage["city"]) #updating the age and city

"""
# Sets 
"""
collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

#collection.remove(1)

collection.pop() # remove random element from the set

print("Set after adding elements:", collection)

print(len(collection))  # Length of the set

"""
# pop method in set
"""
collection = {1, 2, 3, 4, 5}
print(collection.pop() ) # Remove and return an arbitrary element

"""

"""
# set union 

set1 = {1,2,3}
set2 = {2,4,3}

print(set1.union(set2))  # Union of two sets

# set intersection

inter1 = {1,3,5,7}
inter2 = {2,3,4,5}

print(inter1.intersection(inter2))

"""
dis = {
    "table" : " is a piece of furniture with a flat .",
     "cat" : "a small animal"
}
print(dis["table"])
