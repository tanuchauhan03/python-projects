'''The goal here is to build a safe calculator that accepts two numbers from the user, performs addition,
subtraction, multiplication or division, and handles invalid inputs.
Division by zero and unexpected errors very gracefully.'''

def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2==0:
        raise ZeroDivisionError("Cannot divide by")
    return num1/num2

def show_menu():
    print("\n------Calculator Menu------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")

while True:
    show_menu()
    choice=input("Enter your choice:")
    if choice=="5":
        print("Exiting the calculator, Goodbye!.")
        break
    try:
        num1=int(input("Enter a number :"))
        num2=int(input("enter the second number:"))
        if choice=="1":
            print("Result:",add(num1,num2))
        elif choice=="2":
            print("Result:",subtract(num1,num2))
        elif choice=="3":
            print("Result:",multiply(num1,num2))
        elif choice=="4":
            print("Result:",divide(num1,num2))
        else:
            print("Invalid choice , please select avalid option.")
    except ValueError:
        print("Invalid input. please enter valid numbers")
    except ZeroDivisionError as e:
        print(f"Error:{e}")
    except Exception as e:
        print(f"An unexpected error occured:{e}")
    finally:
        print("Thank you for using the safe calculator!... Restarting..")
