# """
# Problem statement - Let user enter login if its code is correct
# """

# code = 1234

# user_input = int(input("Enter the Code = "))

# if user_input == code:
#     print("Successfully logged in")
# else:
#     print("Incorrect code")


"""
Problem Statement - Let a student enter a club if his age is above 18 and reject of his age is under 18 and ask for id proof if his age is 18
"""
age = int(input("enter the age = "))

if age > 18:
    print("you can enter the club")
elif age == 18:
    print("show your id proof to enter")
else:
    print("you are underage")
