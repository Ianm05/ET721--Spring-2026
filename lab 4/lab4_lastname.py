"""
Student's full name
Feb 5, 2026
lab 4, dictionary
"""
print("\n------- Example 1: dictionary ")
# declare and initialize a dictionary
contacts = {
    'Bill':'718-333-4444',
    'Mary':'718-555-6666',
    'John':'718-777-8888'
}
print(f"original dictionary: {contacts}")

# update the value of key Rick
contacts['Rick'] = '347-222-3333'

print(f"updated dictionary: {contacts}")

# add new key-value pair
contacts['Lisa'] = '718-999-0000'

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
# items method returns all the key-value pairs in a dictionary
print(f"items method: {contacts.items()}")
# keys method returns all the keys in a dictionary
print(f"all keys in the dictionary: {contacts.keys()}")
# values method returns all the values in a dictionary
print(f"all values in the dictionary: {contacts.values()}")

print("\n--------- Example 4: check if a key is 'in' or 'not in' a dictionary")
check_name = 'Lucy'
check = check_name in contacts
print(f"Is {check_name} in the dictionary? {check}")

print("\n------- Example 5: Length of a dictionary")
print(f"contacts has {len(contacts)} key-value pairs")

print("\n------- Example 6: remove a pair")
print(f"original dictionary = {contacts}")
contacts.pop('Mary')
print(f"updated dictionary = {contacts}")

print("\n------- Example 7: get method")
# get method returns the value of a key
print(f"key-value pair= {contacts.get('John')}")

print("\n------- Example 8: update method")
# can be used to update a value of a key or to add a new key-value pair
contacts.update({'John':'718-111-2222'})
print(f"{contacts}")
contacts.update({'Lisa':'718-333-4444'})
print(f"{contacts}")
def count_email_domains(emails):
    """
    Count users by email domain (gmail, hotmail, yahoo)
    
    Args:
        emails: List of email addresses or file path
    
    Returns:
        Dictionary with counts for each domain
    """
    counts = {
        'gmail': 0,
        'hotmail': 0,
        'yahoo': 0
    }
    
    # Handle if input is a file path (string)
    if isinstance(emails, str):
        try:
            with open(emails, 'r') as f:
                emails = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: File '{emails}' not found")
            return counts
    
    # Count emails by domain
    for email in emails:
        email_lower = email.lower()
        
        if '@gmail.com' in email_lower:
            counts['gmail'] += 1
        elif '@hotmail.com' in email_lower:
            counts['hotmail'] += 1
        elif '@yahoo.com' in email_lower:
            counts['yahoo'] += 1
    
    return counts


def print_results(counts):
    """Print the domain counts in a formatted way"""
    print("\n" + "="*40)
    print("Email Domain Distribution")
    print("="*40)
    for domain, count in counts.items():
        print(f"{domain.capitalize():15} : {count:5} users")
    print("="*40)
    print(f"{'Total':15} : {sum(counts.values()):5} users")
    print("="*40 + "\n")


if __name__ == "__main__":
    # Example usage with a list of emails
    sample_emails = [
        "user1@gmail.com",
        "user2@hotmail.com",
        "user3@yahoo.com",
        "user4@gmail.com",
        "user5@example.com",
        "user6@yahoo.com",
        "user7@gmail.com",
        "user8@hotmail.com"
    ]
    
    print("Example 1: Counting from a list")
    counts = count_email_domains(sample_emails)
    print_results(counts)