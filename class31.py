'''Abstract Class
Outline:
Write a program to create a base class that consists of two functions - one to display a value,
and another function is an abstract method. Next, create a subclass that consists of a method similar
to the abstract method. Finally, showcase how Abstraction is being implemented in this example.'''
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print(f"Passed value {x}")
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class test_class(Absclass):
    def task(self):
        print("We are inside the test class task.")
test_obj = test_class()
test_obj.task()
test_obj.print(100)
'''Class Animal
Outline:
Write a program to implement abstraction on animal class (base class). The abstract method will be
move will display what subclasses can do. Subclasses can be something like - Human, Dog.'''
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can Walk")
class Snake(Animal):
    def move(self):
        print("I can Slither")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can Roar")
h = Human()
h.move()
s = Snake()
s.move()
l = Lion()
l.move()
d = Dog()
d.move()
    
'''All about Countries
Outline:
Write a program to create two classes for two different countries that consist of three
methods to display the following information of respective country - capital, language and type
of country. Then, use Polymorphism to create a common interface for both classes.'''
class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the national language of India")
    def type(self):
        print("India is A country")
class UAE():
    def capital(self):
        print("Dubai is the capital of UAE")
    def language(self):
        print("Arabic is the national language of UAE")
    def type(self):
        print("UAE is A country")
class USA():
    def capital(self):
        print("New York is the capital of USA")
    def language(self):
        print("English is the national language of USA")
    def type(self):
        print("USA is A country")
c1 = India()
c2 = UAE()
c3 = USA()
for i in (c1, c2, c3):
    i.capital()
    i.language()
    i.type()


