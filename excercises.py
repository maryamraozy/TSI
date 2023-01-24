#Exercise 1
#To practise using variables, update the program you made in the previous modules to print the value of a variable.
#You could use a number (int) or a word (String) for your variable type.
#Be sure to declare the variable and assign it a value before using it in the print() method.

#Exercise 2
#Try writing statements to assign the values below to variables and then use type() inside of print() to 
#discern the type inferred by the python executor and print it to the console.
# 1. 14
a = 14
x = type(a)
print(x)

# 2. Y
b = ("Y")
y = type(b)
print(y)

# 3. Hello!
c = "Hello!"
z= type(c)
print(z)

# 4. 2.5
d = 2.5
z = type(d)
print(z)

# 5. 307
e = 307
z = type(e)
print(z)

# 6. -1
f = -1
z = type(f)
print(z)

# 7. 438000000
g = 438000000
z = type(g)
print(z)

# 8. False
h = False
z = type(h)
print(z)


#Exercise 3
#Multiple 10 with 5, and print the result.  Print(10_5)
print(10*5)

#Exercise 4
#Divide 10 by 5, and print the result. Print(10_5)
print(10/5)

#Exercise 5
#Use the correct operator to increase the value of the variable x by 1. 
# x = 10 | x = x 1
x = 10 
x = x + 1
print(x)

#Exercise 6
#Use the addition assignment operator to add the value 5 to the variable x. 
# x = 10 | x __ 5
x = 10
x += 5
print(x)

#Exercise 7
#Write code to print "Greater" if x is greater than y
# int x = 50; | int y = 10;
x = 50
y = 10
if x > y: print("Greater")

#Exercise 8
#Write code to print "Equal" if x is equal to y. 
# x = 50 | y = 50
x = 50
y = 50
if x == y: print("Equal")

#Exercise 9
#Print "Equal" if x is equal to y, otherwise print "Unequal".
# x = 50 y = 50 | x = 51 y = 49
x = 50
y = 50
print("Equal") if x == y else print("Unequal")

x = 51
x = 49
print("Equal") if x == y else print("Unequal")

#Exercise 10
#Write code to print "1" if x is equal to y, print "2" if x is greater than y, otherwise print "3"
# x = 50 y = 50 | x = 57 y = 50 | x = 5 y = 50
a = 50
b = 50
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

a = 57
b = 50
if a == b:
    print("1")
elif a > b:
     print("2")
else:       
    print("3")

a = 5
b = 50
if a == b:
    print("1")
elif a > b:
    print("2")
else:       
    print("3")

#Exercise 11
#Insert the missing parts to complete the following switch statement. 
day = 2
match  x:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")

#Exercise 12
#Complete the switch statement, and add the correct keyword at the end to specify some code to run if there is no case match in the switch statement
day = 4
match c:
    case 1:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3 | 4 | 5 | 6 | 7:
        print("Weekday")

#Exercise 13
#Use a while loop to print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i +=1

#Create a for loop that prints out numbers 0 to 5, but breaks at the number 3.
for i in range(5):
    if i ==3:
        break    
    print(i)

#Write a while loop that prints out numbers 3 to 8, but skips the number 6.
i = 2
while i < 8:
    i += 1
    if i == 6:
        continue
    print(i)

#Make a nested loop with for loops that prints the values from the following two lists:
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
for number in list1:
    for fruit in list2:
        print(str(number) + " - " + fruit)

#Exercise 14
#What is the results from the two code-segments?
values = [2, 5, 5, 6, 8, 10, 4, 5]
a = 0
while (values[a] <= values[a+1]):
    print(values[a])
    a = a + 1
#Answer = 
# 2
# 5
# 5
# 6
# 8

values = [2, 1, 5, 3, 8, 10, 13, 5]
b = 0
while (b <= values[b]):
    print(values[b])
    b+=1
#Answer = 
# 2
# 1
# 5
# 3
# 8
# 10
# 13