#==============================================================================#
#                         Python Calculator Made By Me                         #
#==============================================================================#

while True:
    print("===========================================")
    print("             Python Calculator             ")
    print("===========================================")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Close App")
    
    choice = input("Enter Your Choice you want that operation (1-5) : ")
    
    if choice == "1":
        print("=====================")
        print("       Addition       ")
        print("=====================")
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter Second number : "))
        sum = number1 + number2
        print(f"Your addition number is {number1} + {number2} = {sum}")
    
    elif choice == "2":
        print("=====================")
        print("     Substraction    ")
        print("=====================")
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter Second number : "))
        sub = number1 -  number2
        print(f"Your Substraction number is {number1} - {number2} = {sub}")
        
    elif choice == "3":
        print("=====================")
        print("    Multiplication   ")
        print("=====================")
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter Second number : "))
        multi = number1 * number2
        print(f"Your Multiplication number is {number1} x {number2} = {multi}")
        
    elif choice == "4":
        print("=====================")
        print("      Division       ")
        print("=====================")
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter Second number : "))
        div = number1 / number2
        print(f"Your Division number is {number1} / {number2} = {div}")
        
    elif choice == "5":
        print("=====================")
        print("       Modulus       ")
        print("=====================")
        number1 = int(input("Enter first number : "))
        number2 = int(input("Enter Second number : "))
        mod = number1 % number2
        print(f"Your Modulus number is {number1} % {number2} = {mod}")
        
    elif choice == "6":
        print("Closing This App........")
        break
    
    else:
        print("Invalid choice")


    