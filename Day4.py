# if else statement
# age=15
# if age<18:
#     print("you can't drive")
# elif age<18 and age>= 17: 
#      print("you can apply for driving ")
# else:
#     print("you can drive")

#number comparison tool

#step 1: get user input for 2 numbers
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))

#step 2: compare the numbers and print the result
print("------Comparison Result------")
if num1>num2:
    print(f"{num1} is Greater than {num2}")
elif num1<num2:
    print(f"{num1} is Smaller than {num2}")
else:
    print("Both Are Equal")