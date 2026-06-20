#simple calculator

#step 1: get user input
name=input("What's your name ?\n")
print(f"Hello {name}!")
num1=float(input("Enter a number :"))
num2=float(input("Enter second number :"))


#4step 2: operations
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2 if num2!=0 else "can't divide by zero"

#step 3: Display result
print("\n------Calculator Results--------")
print(f"Addition       :{num1}+{num2}={add}")
print(f"Subtraction    :{num1}-{num2}={sub}")
print(f"Multiplication :{num1}*{num2}={mul}")
print(f"Division       :{num1}/{num2}={div}")
