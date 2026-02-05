"""
Student's full name
Feb 5, 2026
lab 4, dictionary
"""
print("\n------- Example 1: dictionary ")
# declare and initialize a dictionary
contacts = [
    'Bill':'718-333-4444' ,
    'Mary':'718-555-6666',
    'John':'718-777-8888';
]
print (f"original dictionary: {contacts}")

# update the value of key Rick
contacts ['Rick'] = '347-222-3333'

print(f"updated dictionary: {contacts}")

# add new key-value pair
contacts ['Lisa'] = '718-999-0000'

print(f"updated dictionary with new pair = {contacts}")
# for loop to print each key in the dictionary
for v in contacts:
    print(v)
# for loop to print each value in the dictionary
for v in contacts:
    print(contacts[v])

    # for loop to print each key and value in the dictionary
for v in contacts:
        print(f"{v} phone number is : {contacts[v]}")


        print("\n------- Example 3: items() keys() and values() methods in a dictionary")
# items method retruns all the key-value pairs in a dictionary
print(f"items method: {contacts.items()}")
# keys method returns all the keys in a dictionary
print(f"all keys in the dictionary: {contacts.keys()}"
      # values method returns all the values in a dictionary
print(f"all keys in the dictionary: {contacts.keys()}"\
     

     print (/n--------- Example 4: check if a key is 'in' or 'not in' a dictionary")
    check_name = 'Lucy'
    check= check_name in contacts
    print(f"Is {check_name} in the dictionary? {check}")

    print("\n------- Example 5: Length of a dictionary")
    print(f"contacts has [len(contacts)] key-value pairs")

    print("\n------- Example 6: remove a pair")
    print(f"original dictionary = {contacts}")
    contacts.pop('mary')
    print(f"updated dictionary = {contacts}")  


    print("\n------- Example 7: get method")
    # get method returns the value of a key
    print(f"key-value pair= {contacts.get('John')}")

    print("\n------- Example 8: update method")
    # can be used to update a value of a key or to add a new key-value pair
    contacts.update({'John':'718-111-2222'})
    print(f"{contacts}"
          
    