class Dog:
    def __init__(self, name = "", breed = "", color = "", gender = ""):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    def printAll(self):
        print(f"{self.name}, {self.breed}, {self.color}, {self.gender}")

class BMI:
    def __init__(self, height= 0, weight= 0):
        self.height = height
        self.weight = weight


    def printAll(self):
        print(f"{self.weight /self.height*self.height*703}")

    def bodyMass(self,height, weight):
        self.height = height
        self.weight = weight

class Product:
    def __init__(self, name = "", price = "", quantity = ""):
        self.name = name
        self.price = price
        self.quantity = quantity

    def printAll(self):
        print(f"{self.name}, {self.price}, {self.quantity}")






def main():
    # problem1()
    # problem2()
    # problem3()
     problem4()

# PROBLEM1
# Create a class Dog.
# Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

def problem1():
    puppers = Dog("Optimus Prime", "Sheba Inu", "brownish-yellow", "male")
    puppers.printAll()

# PROBLEM2
# Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.

def problem2():
    once.again = ""
    while (once.again != "="):
        once.again = input("Type in some random keys on your computer. Enter '='.")

# Problem3
# In your main file create three Person objects.
# Change the weight and height of each one. Afterwards,
# print the BMI (body mass index) of each Person.
# If you don’t know how to calculate BMI, look at the code I provided for you.

def problem3():
    client1 = BMI(34,156)
    client2 = BMI(23,167)
    client3 = BMI(24,175)

    client1.gains(37,161)
    client2.gains(25,172)
    client3.gains(27,180)




# Problem4
# Create a class Product that represents a product sold online.
# A product has a name, price, and quantity.
# The class should have changeProduct:
# a) If changeProduct has one parameter, it can change the name of the product.
# b) If changeProduct has two parameters it can change the name and price of the product.
# c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
# Create an object of Product in your problem4 function and print all of it's attributes.

def problem4():


if __name__ == '__main__':
    main()