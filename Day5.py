#loops  for i in range (start,end,step):
for i in range(1,10):
    print(i)

print("----Reverse Loop-----")
for i in range(5,0,-1):
    print(i)
   
print("-----while loop----")
count=5
while count>0:
    print(count)
    count-=1

print("----sleep----")
import time
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year")

#Count Down Timer
#step 1:get user input

start=int(input("Enter the number to start the CountDown from :"))
while start!=0:
    print(start)
    time.sleep(1)
    start-=1


