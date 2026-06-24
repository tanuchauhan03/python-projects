"""In python a function can return value using return.
Syntax : def function_name():
            code
            return value"""
def add(a,b):
    return a+b

result=add(10,20)
print(result)

"""" why use return value ?
Functions become modular and reusable so you can kind of use this anywhere you want.They allow you to process data and return results.
So they use the.
Whoever called this particular function can do whatever it wants with the result, but these functions are the ones that processes the data."""

def rectangle(width,height):
    return width*height
area=rectangle(10,5)
print(area)

def math_operations(a,b):
    addition=a+b
    subtraction=a-b
    division=a/b
    multiplication=a*b
    return addition,subtraction,multiplication,division
result=math_operations(2,8)
print(result)