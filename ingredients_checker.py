#step 1: define the recipe ingredients
recipe_ingredients={"flour","sugar","butter","egg","milk"}
#step 2: get the use input for availble ingredients
user_input=input("Enter the ingredients you have :" )
user_ingredients=set(user_input.split(","))
# step 3: compare ingrefients
missing_ingredients=recipe_ingredients-user_ingredients
extra_ingredients=user_ingredients-recipe_ingredients
#step 4:display results
print("\n----ingredients check Results------")
if missing_ingredients:
    print(f"You are missing the following ingredients : {','.join(missing_ingredients)}")
else:
    print("you have all the ingredients needed.")
if extra_ingredients:
    print(f"You have extra ingredients :{','.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")
