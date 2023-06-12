# #Create a dictionary called "person" with the following 
#key-value pairs: "name" (string) with value "John", "age" (integer) with value 25, 
#"height" (float) with value 1.75, "is_student" (boolean) with value True.
# Add a new key-value pair to the "person" dictionary with
# the key "favorite_color" and the value "blue".
# Access the value of the "age" key in the "person" dictionary and 
#store it in a variable called "person_age".
# Check if the "is_student" key exists in the "person" dictionary.
# Remove the "height" key-value pair from the "person" dictionary.
# Loop through all the key-value pairs in the "person" #
#dictionary and print each key-value pair on a separate line.
# Create a new dictionary called "person2" with the following
# # key-value pairs: "name" (string) with value "Mary", "age" 
#(integer) with value 30, "height" (float) with value 1.6, "is_student" (boolean) with value False.
# Merge the "person" and "person2" dictionaries into a new dictionary called "people".
# Sort the "people" dictionary by age, from youngest to oldest.
# Write a function called "find_person_by_name" 
#that takes a dictionary and a name as arguments and returns the value of the "age" key for the person with that name. 
#If the person is not found in the dictionary, return None.

Person={"name":"JOhn","age":25,"height":1.75,"is_student":True}
print(Person)
Person["favourite_color"]="Blue"
print(Person)
person_age=Person["age"]
print(person_age)
value="is_student" in  Person
print(value)
del Person["height"]
print(Person)

for key,value in Person.items():
    print(f"{key}:{value}")
    

person2={"name":"Mary","age":30,"height":1.6,"is_student":False}
people=dict(Person)
people.update(person2)
print(people)

# Create a dictionary named my_dict with the following key-value pairs:
# "name": "John"
# "age": 25
# "city": "New York"
# Access the value associated with the key "name" in the dictionary my_dict.
# Add a new key-value pair to the dictionary my_dict with the key "country" and the value "USA".
# Change the value associated with the key "age" in the dictionary my_dict to 26.
# Use a loop to iterate over all the keys in the dictionary my_dict and print each key-value pair.


my_dict={"name":"John","age":25,"city":"newyork"}
print(my_dict["name"])
my_dict.update({"country":'USA'})
print(my_dict)
my_dict["age"]=26
print(my_dict)

for key,value in my_dict.items():
    print(key,value)


# Create a dictionary named phonebook with the following key-value pairs:
# "John": "555-1234"
# "Jane": "555-5678"
# "Bob": "555-9012"
# Access the phone number associated with the name "Jane" in the dictionary phonebook.
# Remove the key-value pair associated with the name "Bob" from the dictionary phonebook.
# Use a loop to iterate over all the names in the dictionary phonebook and print each name and phone number.
# Check if the key "Bob" is in the dictionary phonebook

phonebook={
    'John':'555-1234',
    'Jane':'555-5678',
    'Bob':'555-9012',
}
print(phonebook["Jane"])
del phonebook["Bob"]
print(phonebook)

for key,value in phonebook.items():
    print(key,value)

print(phonebook.get('Bob','not there'))


#Write a Python program to create a dictionary from two lists,
#  where one list contains keys and the other contains values.
keys = ["apple", "banana", "cherry"]
values = [1.25, 2.50, 0.75]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)

# Create a dictionary called "person" with keys "name", "age", and "city", and assign values to each key.
# Add a new key called "email" to the "person" dictionary and assign it a value.
# Retrieve the value for the "age" key in the "person" dictionary.
# Remove the "city" key from the "person" dictionary.
# Use a for loop to iterate over the "person" dictionary and print out each key and value.

person={
    "Name":"Rita",
    "age":21,
    "city":"croatia"

}
person.update({"email":"riri@trass"})
print(person)
print(person["age"])
del person["city"]
print(person)

for key,value in person.items():
    print(key,value)

    

       
