"""
What are modules and libraries:
A module is a Python file containing functions, classes, and variables you can reuse in your code.

A library is a collection of modules designed for specific tasks.
"""
#math for maths operations
import math
print(math.sqrt(50))

#here math in the module which we have imported and sqrt is the function inside math madule
#random for random things selection
import random
print(random.randint(1,10))

# from random import choices # specific function
# print(choices["apple","banana","cherry","mango"])

import random as rnd # short form
print(rnd.randint(1,10))

#we also have os and datetime

import random
password =''.join(random.choices('abcdefghijklmnpqrstuvwxyz0123456789',k=8))
print(password)




