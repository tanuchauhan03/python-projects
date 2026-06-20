#step 1: Initialize an empty contact book
contacts={}

#step 2: Display the menu

def show_menu():
    print("\n---Contact Book Menu----")
    print("1. Add contact")
    print("2. view contact")
    print("3. search contact")
    print("4. edit contact")
    print("5. delete contact")
    print("6. contact")

#ste 3: Add a contact
def add_fun():
    name=input("Enter contactname:")
    phone=input("Enter contact Phone Number:")
    email=input("Enter contact email ID:")
    contacts[name]={"phone":phone,"email":email}
    print(f"contact {name} has added to your contact book successfully !")

#step 4: view all contacts
def view_fun():
   if contacts: 
    for name,details in contacts.items():
        print(f"Name:{name}")
        print(f"Phone:{details['phone']}")
        print(f"Email id:{details['email']}")
    else:
       print("your contact book is empty")

#step 5: search a contact
def search_fun():
   name=input("Enter the name of the contact you want to serach :")
   if name in contacts():
      print(f"\n----contacts details for {name}----")
      print(f"Name:{name}")
      print(f"Phone:{contacts[name]['phone']}")
      print(f"Email id:{contacts[name]['email']}")
   else:
      print(f"contact {name} is not found in the book.")

#step 6: edit a contact
def edit_fun():
   name=input("Enter the contact name you want to edit :")
   if name in contacts:
      phone=input("Enter new phone number:")
      email=input("enter new email id:")
      contacts[name]={"phone":phone,"email":email}
      print(f"contact {name } has been updated successfully !")
   else:
      print(f"Contact {name} is not found in the book.")

#step 7: delete a contact
def delete_fun():
   name=input("Enter the contact name you want to delete:")
   if name in contacts:
      del contacts[name]
      print(f"contact {name} has been deleted successfully!")
   else:
      print(f"Contact {name} is not present in the book.")

#step 8: main program
while True:
   show_menu()
   choice=input("Enter your choice:")
   if choice=="1":
      add_fun()
   elif choice=="2":
      view_fun()
   elif choice=="3":
      search_fun()
   elif choice=="4":
      edit_fun()
   elif choice=="5":
      delete_fun()
   elif choice=="6":
      print("Thank you for using the Contact Book. Goodbye!")
      break;
   else:
     print("Invalid choice. please select a valid option (1-6)")

