name = "Pushp"
age = 22


print(name, age)

print(f"you name is {name} and your age is {age}")


"""
NUMERIC TYPE
float - decimal number eg 1.00, 20.52 etc
int - whole number eg 100, 2, etc
complex - real and imaginary part eg a + bi etc

"""

a = 25
b = 2.5

print(type(a))
print(type(b))


"""
BOOL TYPE
True or False
"""

is_raining = True
is_sunny = False

print(is_raining)
print(type(is_sunny))

"""
NONE TYPE
"""

result = None
print(result)


"""
STRING TYPE 
this is immutable datatype

"" - Can be in double quotes
'' - Can be in single quotes
"""

a = "hi pushp"
# a[1] = "H"  # ❌ wrong because string is immutable cannot update at any index but can update the whole string
b = "hello pushp"

print(a)
print(type(a))


"""
LIST TYPE
mutable datatype
eg [1,2,3,4] etc
"""

list1 = [1, 2]
list1 = [1, 2, 3]

list1.append(4)
list1.insert(2, 5)
print(list1)


"""
SET TYPE
mutable datatype
eg {1,2,3,4} etc
"""

set1 = {1, 1, 21, 2}
print(set1)


"""TUPLE TYPE
immutable datatype
eg (1,2,3,4) etc
"""

tupple1 = (1, 2, 2, 3)
# tupple1[0] = 2  # ❌ Wrong because tupple is immutable
print(tupple1)


"""
DICT TYPE
mutable datatype
eg {key : value} etc
"""

dict1 = {"1": "Apple", "2": "Orange", "3": "Banana"}
dict1["2"] = "Banana"
print(dict1)
