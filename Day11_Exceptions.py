#Exceptions: are errors that occur during the execution of a program disrupting its normal flow. python has a built in mechanism for handling errors

# 1. value error : which is raised when an operation receives an argument of a correct type but in a inappropriate value.
#2. zero division error : which is raised when dividing by zero.
#3. type eroor: which is raised when an operation is performed on an inappropriate data type.
#4. filenotfound error

try:
    num=int(input("Enter a number:"))
    result=10/num
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. please enter a valid number.")

"""
try:
    #code that might raise an exception
expect ExceptionType:
    #code to handle the exception
else:
    #execute if no exception occurs
finally:
    #always execute , even if an exception occurs

"""


#one exception
try:
    num=int(input("Enter a number:"))
    result=10/num
    print("result:",result)
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
else:
    print("No exception occured. Result:",result)
finally:
    print("finally block executed.")


#handling multiple exception
try:
    num=int(input("Enter a number:"))
    result=10/num
except (ZeroDivisionError,ValueError):
    print("ERROR: division by zero or invalid input")


#Raising custom exception 
def withdraw(amount):
    if amount<0:
        raise ValueError("Invalid withdrwal amount- amount can't be negative")
try:
    withdraw(-50)
except ValueError as e:
    print(e)

