from abc import ABC, abstractmethod


class Dog:
    species = "Canine"  # Class attribute, static variable.

    def __init__(self, name, age):
        """
        __init__ method is the constructor
        """
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

# Access instance and class attributes
print(dog1.name, dog1.age, dog1.species)
# Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)  # Access class attribute directly

# Single Inheritance


class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")


# Multilevel Inheritance


class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")


# Multiple Inheritance


class Friendly:
    def greet(self):
        print("Friendly!")


class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")


# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


# Diamond problem resolution in Python
# Method Resolution Order (MRO) based on the C3 linearization algorithm,
# This algorithm imposes a strict, depth-first, left-to-right order that
# prevents ambiguity when searching for a method in the inheritance hierarchy.
class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()  # Calls the next method in the MRO (A.greet)


class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()  # Calls the next method in the MRO (A.greet)


class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()  # Calls the next method in the MRO (B.greet)


d_instance = D()
print(D.mro())
d_instance.greet()


# Compile-Time Polymorphism
# True compile-time polymorphism is not supported.
# Instead, Python mimics it using default arguments or *args/**kwargs.
# Operator overloading can also be seen as part of polymorphism, though it is implemented at runtime in Python.

# Run-Time Polymorphism is determined during the execution of the program. It covers multiple forms in Python:
# Method Overriding: A subclass redefines a method from its parent class.
# Duck Typing: If an object implements the required method, it works regardless of its type.
# Operator Overloading: Special methods (__add__, __sub__, etc.) redefine how operators behave for user-defined objects.
# Method Overriding
# We start with a base class and then a subclass that "overrides" the speak method.


class Animal:
    def speak(self):
        return "I am an animal."


class Dog(Animal):
    def speak(self):
        return "Woof!"


print(Dog().speak())

# 2 Duck Typing


class Cat:
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()


print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))

# 3 Operator Overloading
# We create a simple class that customizes the '+' operator.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # This special method defines the behavior of the '+' operator.
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)

# Encapsulation


class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

print("# Data Abstraction ")
# Data Abstraction


class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    # A decorator is a function that wraps another function
    # (Modify behavior of functions, Without changing their source code)
    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")


class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")


class Beagle(Dog):  # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")


# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method

# Interface (Full Abstraction: Abstract class contains only abstract methods)

# Define the interface


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# Implement the interface


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")


# Attempting to instantiate an incomplete class raises an error


class IncompleteCar(Vehicle):
    def start_engine(self):
        print("Engine started, but can't stop")


# This will raise a TypeError: "Can't instantiate abstract class IncompleteCar with abstract method stop_engine"
try:
    my_incomplete_car = IncompleteCar()
except TypeError as e:
    print(f"Error: {e}")

# This works correctly
my_car = Car()
my_car.start_engine()


# Operator Overloading in Python (https://www.geeksforgeeks.org/python/operator-overloading-in-python/)

# staticmethod
# Python program to
# demonstrate static methods


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


res = Person.isAdult(12)
print("Is person adult:", res)

res = Person.isAdult(22)
print("\nIs person adult:", res)
