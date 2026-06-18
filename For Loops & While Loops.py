"""
While loop - finishes after a certain condition is met
For loop - iterate for a given time or range
"""

# WHILE LOOP EXAMPLE
i = 1
while i <= 10:
    print(i)
    i = i + 1


# FOR LOOP EXAMPLE
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    print(i)


# FOR LOOP IN RANGE EXAMPLE

for i in range(10):  # Will always start from 0
    print(i)

for i in range(1, 10):  # Starting value
    print(i)

for i in range(1, 10, 2):  # Gap after each iteration
    print(i)


"""
Continue and Brea and Pass statements

continue - To skip an iteration
break - To exit a loop when a condition is met
pass - do nothing 
"""

for i in range(1, 10):
    if i == 5:
        continue  # Skips 5
    print(i)


for i in range(1, 10):
    if i == 5:
        break  # Exits the loop at 5

    print(i)


for i in range(1, 10):
    if i == 5:
        pass  # Simply iterates on 5 too and will do nothing
    print(i)
