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
    print(f"{name} added to the group")

def get_average_ages(my_group):
    """
    Calculates the average (mean) age of the group
    """
    ages = [person["age"] for person in my_group]
    return np.mean(ages)

def forget_person(person1, person2):
    """
    Removes a relationship between two people, ensuring it is removed from both sides.
    """
    for person in my_group:
        if person['name'] == person1 and person2 in person["Relationships"]:
            del person["Relationships"][person2]
    for person in my_group:
        if person['name'] == person2 and person1 in person["Relationships"]:
            del person["Relationships"][person1]

def safe_get(person, key):
    """
    Safely retrieves the value for the specified key, returning None if the key does not exist.
    """
    try:
        return person[key]
    except KeyError:
        return None
    
if __name__ == "__main__":
    # Initialize the group
    my_group = rows.copy()

    # Calculate the average age of the group
    mean_ages = get_average_ages(my_group)
    print("Average age of group = ", mean_ages)

    # Calculate and print the maximum age in the group
    max_age = max(person["age"] for person in my_group)
    print('Maximum age = ', max_age)

    # Calculate the average number of relationships per person
    num_relationships = [len(person["Relationships"]) for person in my_group]
    print("Average number of relationships = ", np.mean(num_relationships))

    # Find the maximum age of people with at least one relationship
    max_age_with_relations = max(person["age"] for person in my_group if len(person["Relationships"]) >= 1)
    print('Maximum age of people with at least one relationship = ', max_age_with_relations)

    # Advanced: Find the maximum age of people who have at least one friend
    max_age_with_friends = max(
        person["age"] for person in my_group if sum(1 for value in person["Relationships"].values() if value == "Friend") >= 1
    )
    print('Maximum age of people with at least one friend = ', max_age_with_friends)