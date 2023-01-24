#what is a class?
# It is a blueprint for creating an object. For example to a person class would store information about the person
#what is an object?
#An object is an instance of the class. In this example, in the person class it would contain information like the person's gender, age, height, hair colour. 
#how are these two concepts related?
#one class can have many objects and the value of properties for different objects can be different 

#Exercise 1
#Insert the missing part to call myMethod() from main().
def myMethod():
    print("I just got executed!")

if __name__ == "__main__":
    myMethod()

# Outputs "I just got executed"

#Exercise 2
#Write a program with a method named getTotal() that accepts two integers as an argument and return its sum. Call this method and print the results.
def getTotal(number1, number2):
    return number1+number2

if __name__ == "__main__":
    result = getTotal(34,56)
    print("number 1 and number 2 equal to:", result)

#Exercise 3
#Create a car class with the atributes model and color
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

#Exercise 4
#Complete the code to instantiate an object of the Car class, and output its model and color.
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def print_info(self):
        print("Model: " + self.model)
        print("Color: " + self.color)

if __name__ == "__main__":
    my_car = Car("BMW", "Red")
    my_car.print_info()

#Exercise 5
#Write a python program to create a dictionary containing exam results, where the keys are students names, and the values are lists of their results (as numbers).
#Then iterate over the exam results dictionary and output the highest score of each student. 
exam_results = {
    "Anna": [67, 56],
    "Ben": [85, 78],
    "Chris": [50, 65],
    "Delilah": [79, 87],
    "Ellie": [90, 85],
    "Felix": [45, 56]
}
maximum = max(exam_results, key=exam_results.get)
print(maximum, exam_results[maximum])

#Exercise 6 
# Using the results dictionary from the previous exercise, write a dict comprehension that produces a dictionary mapping student names to their average scores. 
exam_results = ["Anna", "Ben", "Chris", "Delilah", "Ellie", "Felix"]
for k,v in exam_results.iteritems():
    col_average = { exam_results.append(sum(v)/float(len(v))) in exam_results}

print(col_average)