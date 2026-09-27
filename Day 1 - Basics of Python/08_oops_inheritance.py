class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog1 = Dog()
dog1.eat()
dog1.bark()