"""
CLASSES - A Blueprint for creating an object
CONSTRUCTOR - Method of a class that invokes when object is created
"""

# class Car():
#     name : str
#     colour : str
#     brand : str

#     def __init__(self, name, colour, brand):          # Constructor
#         self.name = name
#         self.colour = colour
#         self.brand = brand


# car1 = Car(name="BMW", colour="Black", brand="BMW")
# print(car1.name)


"""
Polymorphysm - Same name but different fucntionality
"""

# class Bird():
#     sound : str

#     def __init__(self, sound):
#         self.sound = sound


# class Crow(Bird):
#     def sound(self):
#         print('Crow says "Caw Caw"')

# class Parrot(Bird):
#     def sound(self):
#         print("Parrot says 'Squake'")


# bird1 = Crow(sound="Caw caw")
# bird2 = Parrot(sound="Squake")

# print(bird1.sound)
# print(bird2.sound)


class Bird:

    def sound(self):
        print("Bird says sound")


class Crow(Bird):
    def sound(self):
        print('Crow says "Caw Caw"')


class Parrot(Bird):
    def sound(self):
        print("Parrot says 'Squake'")


bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()
