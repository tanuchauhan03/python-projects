#list is a collection of items stored in a single variable . they are mutable and indexed
shopping_list=["milk","eggs","bread"]
print(shopping_list)

#list opertaions
print(shopping_list[2]) #index 2

#append add the item at the end of the list
shopping_list.append("Butter")
print(shopping_list)

#insert requires position 
shopping_list.insert(1,"juice")
print(shopping_list)

#remove : removes requires name of the item to remove 
shopping_list.remove("Butter")

#whereas pop delete the item from the end of the list
shopping_list.pop()
print(shopping_list)

#for loop in list
for item in shopping_list:
    print(item)

# methods : shopping_list.sort(),shopping_list.reverse(),shopping_list.clear()
print("---Shopping List App-----")

#step 1: Initialize an empty shopping list
Shopping_List=[]
#step 2: Define the main menu
def show_menu():
    print("\n--shopping list menu----")
    print("1.View the shopping List")
    print("2.Add an item")
    print("3.Remove an item")
    print("4.Clear List")
   
    print("5. Exit")
#step 3: main program loop
    
