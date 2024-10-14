"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import numpy as np
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

def add_person(name, age, job=None, relationships=None):
    """
    Adds a new person to the group.
    Note that relationships will be a dictionary, with the other person being the key and then the relationship, e.g. {"Person's Name": "type of relationship"}
    Example:
    add_person("Dave", 63, relationships={"Jill": "Dad", "John": "Father in law"})
    """
    person = {"name": name,
        "age": age,
        "job": job if job else None,
        "relationships" : relationships if relationships  else {}
        }
    my_group.append(person)
    print(name, 'added to the group')

def get_average_ages(my_group):
    """
    Calculates the average (mean) age of the group
    """
    ages = []
    [ages.append(person["age"]) for person in my_group]
    return np.mean(ages)

def forget_person(person1, person2):
    for person in my_group:
        if person['name'] == person1:
            del person["Relationships"][person2] 


my_group = []
for row in rows:
    # for key, entry in enumerate(row):
    #     print(entry, row[entry])
    my_group.append(row)

#mean age of the group
mean_ages = get_average_ages(my_group)
print("Average age of group = ", mean_ages)

#'forget' a relationship
#forget_person("Jill", "John")

#what is the maximum age in the group?
ages = []
[ages.append(person["age"]) for person in my_group]
print('Maximum age = ', max(ages))

#the average (mean) number of relations amoung the members of the group
num_relationships = []
[num_relationships.append(len(person["Relationships"])) for person in my_group]
print(np.mean(num_relationships))

#the maximum age of people in the group that have at least one relation
ages = []
for person in my_group:
    if len(person["Relationships"]) >=1:
        ages.append(person["age"])
print(max(ages))

#[more advanced] the maximum age of people in the group that have at least one friend
ages = []
for person in my_group:
    if sum(1 for value in person["Relationships"].values() 
    if value == "Friend") >=1:
        ages.append(person["age"])
print(max(ages))

