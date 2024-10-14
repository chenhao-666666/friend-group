"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = 1


"""
rows = [{ "name": "", "age": "", "job": "", Relationships: {} }, 
        ]
"""
rows = [
        { "name": "Jill", "age": "26", "job": "biologist", "Relationships": {"Friends": ["Zalika"],  "Partner": ["John"]}},
        
        { "name": "Zalika", "age": "28", "job": "artist", "Relationships": {"Friends": ["Jill"]}, "Landlord": ["Nash"]}, 
        
        { "name": "John", "age": "27", "job": "writer", "Relationships": {"Partner": ["Jill"]}, "Cousins": ["Nash"]}, 

        { "name": "Nash", "age": "34", "job": "chef", "Relationships": {"Cousins": ["John"], "Landlord for": ["Zalika"]}},          
        ]

# group_of_friends = []

# for person in rows:
#     group_of_friends.append(person)
#     if person["Relationships"] == None:

def add_person(name, age, job=None, relationships=None):
    person = {"name": name,
        "age": age,
        "job": job if job else None,
        "relationships" : relationships if relationships  else {}
        }
    return person


for row in rows:
    for key, entry in enumerate(row):
        print(entry, row[entry])


#add

    