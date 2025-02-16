# lists in python
# food  = ["pizza", "hamburrger", "hotdogs", "spaghetti", "pudding"]
# food[0] = "sushi"

# print(food)
# food.append("ice cream")
# print(food)
# food.remove("hotdogs")
# print(food)
# food.insert(0,"cake")
# print(food)
# food.sort()
# print(food)
# food.clear()
# print(food)

# for x in food:
#     print(x)

# variable scope 

# name = " bro"
# def display_name():
#     name = 'Code'
#     print(name)

# display_name()
# print(name) 

# priority 
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# args parameter in python
# *args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments

# def add(num1,num2):
#     sum = num1 + num2
#     return sum

# if we pass 3 arguments instead of 2 we get an error
# to fix that we use *args

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i  # This will correctly add all values in args
#     return sum

# print(add(1,2,3))

# **kwargs = parameter that will pack all arguments into a dict

# def hello(first,last):
#     print("Hello " + first + " " + last)

# hello(first="Bro", middle = "Dude", last="Code")

# solution to fix the above

# def hello(**kwargs):
#     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello" , end=" ")
#     for key,value  in kwargs.items():
#         print(value, end=" ")
# hello(title = "mister" , first="Bro", middle = "Dude", last="Code")

# exception = events detected during execution that interrupt the flow of a progam 

# try:
#     numerator = int(input("Enter a number to divie: "))
#     denominator = int(input("enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# # if somebody tries to divide by zero
# except ZeroDivisionError:
#     print("you cant divide by zero, idiot!")
# # if somebody tries to divide by anything other than a number
# except ValueError:
#     print("you can only divide by a number, dumbo!")

# except Exception:
#     print("something went wrong!!")
# else:
#     print(result)
# finally:
#     print("This will always execute")

import os 
path = './test.txt'

# if os.path.exists(path):
#     print("that location is correct")
# else:
#     print("the location may not be correct one!")

# reading from a file
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)

