"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

"""
rows = [{ "name": "", "age": "", "job": "", Relationships: {} }, 
        ]
"""
rows = [
        { "name": "Jill", "age": 26, "job": "biologist", "Relationships": {"Zalika": "Friend", "John": "Partner"}},
        
        { "name": "Zalika", "age": 28, "job": "artist", "Relationships": {"Jill": "Friend", "Nash": "Landlord"}}, 
        
        {"name": "John", "age": 27, "job": "writer", "Relationships": {"Jill": "Partner", "Nash": "Cousin"}}, 

        { "name": "Nash", "age": 34, "job": "chef", "Relationships": {"John": "Cousin", "Zalika": "Tenant"}},          
        ]

my_group = []
def add_person(name, age, job=None, relationships=None):
    person = {"name": name,
        "age": age,
        "job": job if job else None,
        "relationships" : relationships if relationships  else {}
        }
    my_group.append(person)
    print(name, 'added to the group')

for row in rows:
    # for key, entry in enumerate(row):
    #     print(entry, row[entry])
    my_group.append(row)

#what is the maximum age in the group?
ages = []
[ages.append(person["age"]) for person in my_group]
print(max(ages))

