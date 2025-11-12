"""
Henry Perez
Lab 4, Dictionary and Functions
September 10th, 2025
"""

print("----- Example 1: Dictionary -----")
# contact dictionary with three different users
contacts = {
    "Bill": "(718)111-2222",
    "Martha": "(646)000-3333",
    "Peter": "(212)000-1111",
}
print(contacts)
# Save the Value of a specific key
user1 = contacts["Martha"]
print(f"User's phone number = {user1}")

# add new content to the dictionary
contacts["Anna"] = "(646)222-3333"
print(contacts)

# update value of a specific key
contacts["Peter"] = "(800)000-0000"
print(contacts)

# print each value in the dictionary
print("----- Example 2: Loop throguh a dictionary -----")
for i in contacts:
    print(contacts[i])

# print each key:value in the dictionary
for i in contacts:
    print(f"{i}={contacts[i]}")

print("----- Example 3: length of a dictionary -----")
print(f"Dictionary has {len(contacts)} users")

print("----- Example 4: Copy a dictionary -----")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(copy_contact1)
print(copy_contact2)

print("----- Example 5: Remove a key:value pair  in a dictionary -----")
print(contacts)
contacts.pop("Peter")
print(contacts)
contacts.popitem()
print(contacts)

print("----- Example 6: Add a new key:value pair in a dictionary")
print(contacts)
contacts.update({"Lucas": "(212)111-1111"})
print(contacts)

print("----- Example 7: Return items, keys, and values on a dictionary -----")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("----- Example 8: Dictionary application -----")
# store in a dictionary the count of occurency of the words in a phrase
phrase = "to be or not to be"
list_phrase = phrase.split()
# create an empty dictionary
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# print result
for word in word_count_dict:
    print(f"{word} appears {word_count_dict[word]}")

print("----- EXERCISE -----")
users = [
    "peterpan@yahoo.com",
    "annie@hotmail.com",
    "carl@hotmail.com",
    "martha@gmail.com",
    "cassie@yahoo.com",
    "josue@hotmail.com",
    "john@hotmail.com",
]
email_count_dict = {"@gmail.com": 0, "hotmail.com": 0, "@yahoo.com": 0}
for user in users:
    if "gmail.com" in user:
        email_count_dict["@gmail.com"] += 1
    elif "hotmail.com" in user:
        email_count_dict["hotmail.com"] += 1
    elif "yahoo.com" in user:
        email_count_dict["@yahoo.com"] += 1

print(email_count_dict)
