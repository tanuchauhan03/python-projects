def celsius_fahrenheit(celsius):
    return (celsius*9/5)+32
def celsius_kelvin(celsius):
    return celsius+273.15
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit-32)*5/9
def fahrenheit_kelvin(fahrenheit):
    return (fahrenheit-32)*5/9+273.15
def kelvin_celsius(kelvin):
    return kelvin-273.15
def kelvin_fahrenheit(kelvin):
    return (kelvin-273.15)* 9/5+32
def show_menu():
    print("-----Tempreture converter Menu----")
    print("1.celsius to fharenheit and Kelvin")
    print("2.fharenheit to celsius and kelvin")
    print("3.kelvin to celsius and fahrenheit")
    print("4.EXIT")
while True:
    show_menu()
    choice=input("Enter your choice:")
    if choice=="1":
        c=float(input("Enter temperature in celcius:"))
        print(f"Fahrenheit :{celsius_fahrenheit(c)}")
        print(f"Kelvin:{celsius_kelvin(c)}")
    elif choice=="2":
        f=float(input("Enter temperature in fahrenheit:"))
        print(f"Celsius:{fahrenheit_celcius(f)}")
        print(f"Kelvin:{fahrenheit_kelvin(f)}")
    elif choice=="3":
        k=float(input("Enter temperature in kelvin:"))
        print(f"Ceksius:{kelvin_celsius(k)}")
        print(f"Fahrenheit:{kelvin_fahrenheit(k)}")
    elif choice=="4":
        print("Thank you for using Temperature converter . Goodbye!.")
        break;

