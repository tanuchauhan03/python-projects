#functions are reuseable bloack of code that makes code clener ,break large task into smaller tasks
def Hello():
    print("hello from the function")
Hello()

#parameters
def greet_user(name):
   print(f"Hello, {name} !Wecome to python")
greet_user('alice')

#Function to add two numbers
def add(a,b):
    print(f"Sum of {a} + {b} :" ,a+b)
add(5,7)

print("----Return statement-----")
def multiply(a,b):
    return a*b
result=multiply(5,3)
print("The result is :", result)

print("---basic maths quiz game------")
#step 1: define the math question function
import random
import operator
def generate_question():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice('+','-','*')
    if operator=='+':
      answer=num1+num2
    elif operator=='-':
      answer=num1-num2
    else:
      answer=num1*num2
      return f"{num1} {operator} {num2}",answer

#step 2: main quiz game function
def math_quiz():
   score=0
   rounds=5
   print("\n--Welcome to the Math Quiz Game !--")
   print("You will be presentes with math problems,and you need to provide the correct answers.")
   for i in range(rounds):
      question,correct_answer=generate_question()
      print(f"\nQuestion {i+1}:{question}")
      user_answer=int(input("Your answer :"))
      if(user_answer==correct_answer):
         print("correct")
         score+=1
      else:
         print(f"Wrong! the correct answer is : {correct_answer}")

   print("\n--game over!--")
   print(f"Your final score is :{score}/{rounds}")
   if score==rounds:
      print("Congratulations! you get all the questions coreect.")
   elif score>=rounds//2:
      print("Godd job! you did well.")
   else:
      print("Keep practicing ! you can do better next time.")
math_quiz()