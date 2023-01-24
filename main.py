#code - hello world 
if __name__ == '__main__':
    print("Hello World!")
#code - print your name
if __name__ == '__main__':
    print("MARYAM")

print(2 + 3)
x = 5
y = 5
z = x + y

X = 3
Txt = "hello"
print (X)
print (Txt)

# code - using the same variable, the later x will override the x = 3 which is referenced on the print screen
x = 3
x = 7
print (x)

print(10_5)

#if statements
x = 1
y = 2
if x == 1:
    print("x is equal to 1")
if y == 1:
    print ("y is equal to 1")

#else statements
x = 2
if x == 1:
    print ("x is equal to 1")
else: 
    print ("x is not equal to 1")

#else if
x = 3
if x == 1:
    print ("1")
elif x == 2:
    print ("2")
elif x == 3:
    print ("3")
else: 
    print("Other number")

#short hand if statements
x = 1
y = 2
if y > x: print(" y is greater than x")

#short hand if else statements
x = 2
y = 1
print("y") if y > x else print("x")

#multiple short hand if else statements
x = 1
y = 1
print("y") if y > x else print("x equals y") if x == y else print("x")

#the and keyword one or two conditions have to be true
x = 1
y = 2
if x == 1 and y == 2:
    print("both conditions are true")

#the or keyword, you dont need both conditions to be true
x = 1
y = 2
if x == 1 or y == 3:
    print ("either or both conditions are true")

#nested if statements
x = 10
if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("and also greater than 10")
    else:
        print("but not greater than 10")

#the pass statement
x = 1
if x ==1:
    pass

#match statement
x = 3
match x:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3 | 4 | 5:
        print("3 or 4 or 5")
    case _:
        print("other number")

#while loop
i = 5
while i <= 10:
    print(i)
    i += 1

#infinite loop
# i = 5
# while i <= 10:
#   print 10

#for loop
for x in "hello":
    print (x)

#the range function
for i in range(6):
    print(i)

#the break statement
#while loop
i = 1
while i <6:
    print(i)
    if i == 3:
        break
    i +=1
#For loop
for i in range(6):
    print(i)
    if i ==3:
        break

#the continue statement
#while loop
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print(i)

#for loop
for i in range(4):
    if i == 2:
        continue
    print(i)

#the pass statement 
#while loop
i = 0
while i < 6:
    i += 1
    pass
#for loop
for x in[0, 1, 2]:
    pass

#else statement
#while loop
i = 0
while i < 3:
    print(i)
    i +=1
else:
    print("Ended")
#For loop
for i in range(3):
    print(i)
else:
    print("Ended")

#nested loops 
list1 = [1, 2]
list2 = ["a", "b"]
for number in list1:
    for letter in list2:
        print(str(number) + " - " +)
#Lists
cars = ["volvo", "BMW", "Ford", "Mazda"]
print(cars[0])

cars[0] = "Opel"
cars = ["volvo", "BMW", "Ford", "Mazda"]
print(cars[0])

#Methods - very similar to a function
#Creating a method
def minFunction(n1, n2):
    min = 0
    if (n1 > n2):
        min = n2
    else :
        min = n1
    return min 

#Calling a method
#def myMethod():
 #     print ("I just got executed!")

#if __name__

#def

#Tuples
myTuple = ('hello', 'hello')

#need to paint a wall but dont know how much paint needed to paint a wall. measuring tape, how much something measures. 



#OOP - think about objects
# Dont repeat yourself
# class is a template for objects, and object is an instance of a class
# create a class
class MyClass:
    def __init__(self):
        self.num = 3
        self.message = "Hello"
#create a object
def main():
    my_object = MyClass()
    print(my_object.message)

if __name__ == '__main__':
    main()
#class attributes
class Item
    def __init__(self):
        self.cost = 4.99
        self.color = "Green"

if __name__ == '__main__':
    my_item = Item()
    print("Item color:", my_item.color)

#modify - change line 238 
my_item.cost = 5.99
print(my_item.cost)

#attributes with multiple objects
#same class Item
if __name__ == '__main__':
    item1 = Item()
    item2 = Item()
    item1.cost = 5.99
    print(item1.cost)
    print(item2.cost)

#class methods
#same class Item
    def say_color(self):
        print(f"I'm a {self.color} item!")

if __name__ =='__main__':
    my_item = Item()
    my_item.say_color()

#constructors
#use class item
    def __init__(self, cost, color)
        self.cost = cost
        self.color = color
#use method say_color
    def say_color(self):
        print(f"I'm a {self.color} item!")

if __name__ == '__main__':
    item1 = Item(3.5, "Blue")
    item2 = Item(0.42, "Red")
    item1.say_color()
    item2.say_color()

#OOP Principles
#inheritance, abstraction, polymorhism, encapsulation
#inheritance - involves one object of a class acquiring the behavior and properties
class Mammal:
    def run(self):
        print("Running!")

class Dog(Mammal):
    def bark(self):
        print("Wolf!")

if __name__ == "__main__":
    spot = Dog()
    spot.run()
    spot.bark()

#multiple inheritance

class Mammal:
    def eat(self):
        print("Eating!")

class Vehicle:
    def move(self):
        print("Moving!")

class Horse(Mammal, Vehicle):
    def makeNoise(self):
        print("Neigh!")

if __name__ == "__main__":
    seabiscuit = Horse()
    seabiscuit.eat()
    seabiscuit.move()
    seabiscuit.makeNoise()

#inheritance - super (different implementation of the same method)
#helps make code more reusable, able to reuse attributes

class Dog:
    def bark(self):
        print("Woof!")

class Spot(Dog):
    def bark(self):
        super().bark()
        print("Ruff!")

if __name__ == "__main__":
    spot = Spot()
    spot.bark()

#Abstraction - involves only exposing relevant information about an entity, and "hiding" the rest
# able to use ABC - abstract base class module.
# @abstract method - to declare methods

from abc import ABC, abstractmethod

class Flower(ABC):
    @abstractmethod
    def bloom(self):
        pass

    def grow(self):
        print("Growing...")

class Dandelion(Flower):
    def bloom(self):
        print("Yellow Flower")

if __name__ == "__main__":
    dandy = Dandelion()
    dandy.grow()
    dandy.bloom()

#Polymorphism and Encapsulation
#polymorphism - many forms, when there are many classes that implement the same class and methods
#dynamically typed 
#goes hand in hand with inheritance

from abc import ABC, abstractmethod

class Flower(ABC):
    @abstractmethod
    def print_color(self):
        pass

class Dandelion(Flower):
    def print_color(self):
        print ("Yellow")

class Rose(Flower)
    def print_color(self):
        print("Red")

if __name__ == "__main__":
    dandy = Dandelion()
    rose = Rose()
    flowers = [dandy, rose]
    for flower in flowers:
        flower.print_color()

#Encapsulation - making things private or public. 
# controlling outside access to class data
# 3 levels - public, protected and private
class MyClass:
    def __init__(self):
        self.foo = "public" #accessible anywhere
        self._bar = "protected" #accessible in class and subclasses
        self.__baz = "private" # accessible in class only

#Get and Set
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self.name = name

#Dictionaries
#python's dict type is a way to store a set of key/value pairs. Can be any immutable type. 
my_dict = {
    "foo": 42,
    "bar": "baz"
}

print(my_dict["foo"])
my_dict["new_key"] = True

#iterating over dictionaries
my_dict = {
    "foo":42
    "bar": "baz"
}

for key in my_dict.keys():
    value = my_dict[key]
    print(f"{key=}{value=}")

for key, value in my_dict.items():
    print(f"{key=}{value=}")

#dictionary comprehension

colors = ["red", "green","blue"]
col_lengths = {col: len(col) for col in colors}

print(col_lengths)
#output: {'Red':3, 'Green':5, 'Blue':4}

#
