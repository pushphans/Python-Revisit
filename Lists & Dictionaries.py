"""
LIST
"""

list1 = [1, 2, 3]

list2 = list1

print(list1, list2)  # Same data in both list
list2[1] = 5  # Changing list2 affects list1 as well
print(list1, list2)  # Both lists changed

# We use copy() to avoid this by cloning list 1 in list 2 and then we can separately alter both lists
list1 = [1, 2, 3]

list2 = (
    list1.copy()
)  # This will clone list 1 into list 2 and then we can alter list 2 without effecting list 1

list2[1] = 5  # Updated list 2 not list 1
print(list1, list2)  # both lists have different data now


"""
DICT
"""

profile = {"name": "ABC", "age": 30, "salary": 500000.00}

# get() - used to retrieve value of a key
age = profile.get("age", "Key not found")
print(age)


# keys() - used to get all keys in a dict
keys = profile.keys()
print(keys)
print(list(keys))

# values() - used to get all values in a dict
values = profile.values()
print(values)
print(list(values))


# items() - used to get all key-value pairs in a dict
items = profile.items()
print(items)
print(list(items))

# pop() - takes the key and return the removed element
popped = profile.pop("age", "key not found")
print(popped)
print(profile)
