1. Inheritance

A child class can reuse the methods and variables of its parent class.

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

d = Dog()
d.eat()      # Eating

Remember: The child automatically gets the parent's methods.

# ---x----x-----

2. Method Overriding

The child class can replace a method from the parent class.

class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Woof")

Dog().speak()      # Woof

Remember: If the child has the method, Python uses the child's version.

# ---x----x----

3. super()

super() lets the child call the parent's method before or after adding its own behavior.

class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

Dog().speak()

Output:

Animal
Woof

Remember: super() = "Run the parent's version."

# -----x-----x----

4. super().__init__()

Used to initialize the parent class when the child has its own constructor.

class Person:
    def __init__(self):
        print("Person Created")

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student Created")

Student()

Output:

Person Created
Student Created

Remember: Without super().__init__(), the parent's constructor won't run.


# -----x-----x---

5. Class vs Object

class Car:
    pass

print(type(Car))     # <class 'type'>

c = Car()
print(type(c))       # <class '__main__.Car'>

Remember:

Car → Class (Blueprint)
Car() → Object (Instance)
