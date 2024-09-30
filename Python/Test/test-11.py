# #Q1.Yash now learned how he could use inheritance to create a square class
# with the help of the existing rectangle class. Now with the help of method
# overriding, he wants to change the side of the squares as well. He just
# need to redefine the method setLength( ) and setBreadth( ).
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def setLength(self, length):
        self.length = length

    def setBreadth(self, breadth):
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
    def setLength(self, side):
        self.length = self.breadth = side

    def setBreadth(self, side):
        self.length = self.breadth = side

    def setSide(self, side):
        self.setLength(side)
        self.setBreadth(side)


sq = Square(4)
print(sq.area())

sq.setSide(5)
print(sq.area())

# #Q2. In a town, a garage owner manages cars and motorcycles. The owner
# needs a program to track vehicle operations. Cars honk when started;
# motorcycles pop wheelies when started. The owner wants to start and
# stop vehicles as requested. Instructions for the code: Create a Python
# program with classes for Vehicle, Car, and Motorcycle as shown. Define
# attributes and methods for starting and stopping vehicles. Create
# instances of Car and Motorcycle. Demonstrate starting, performing
# vehicle-specific actions, and stopping both instances. Ensure the
# program runs without errors and showcases vehicle functionalities.
class Vehicle:
    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")


class Car(Vehicle):
    def start(self):
        print("Car started and honks.")

    def stop(self):
        print("Car stopped.")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started and pops a wheelie.")

    def stop(self):
        print("Motorcycle stopped.")

car = Car()
motorcycle = Motorcycle()

print("Car operations:")
car.start()
car.stop()

print("\nMotorcycle operations:")
motorcycle.start()
motorcycle.stop()

