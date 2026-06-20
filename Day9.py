#Tuples and Sets
#tuples: a tuple is a immutable  data structure in python. acn not be chnaged add or removed . used for storing fixed collection.tuples are faster than list
my_tuples=(1,2,3)
fruits=("apple","banana","cherry") #(0,1,2) or (-3,-2,-1)
print(fruits[0])
print(fruits[-1])
#tuple operations 
print(len(fruits))
print(fruits+("orange",))

#sets :list of items . can not add duplicate 
my_set={1,2,3 }
ingredients={"flour","sugar","butter"}
print(ingredients)
ingredients.add("eggs")
ingredients.remove("sugar")
print(ingredients)
#set operation:union,intersection,difference
set_a={"flour","bread","butter"}
set_b={"sugar","eggs","butter"}
print(set_a | set_b) #union
print(set_a & set_b) #intersection 
print(set_a - set_b) #difference