"""
List Comprehensions :List Comprehension provide a concise way to create and manipulate lists using a single line of code. 
Syntax: [expression for item in iterabe if condition]"""
squares=[x**2 for x in range(10)]
print(squares)

number=[1,2,3,4,5]
double=[x*2 for x in number]
print(double)

even=[x for x in number if x%2==0]
print(even)

odd=[x for x in number if x%2!=0]
print(odd)

names=["tanu","vaibhav","kamni","anshul"]
filter=[name for name in names if(len(name)<5)]
print(filter)
