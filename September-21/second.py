while True:
    print("1. Sum")
    print("2. Substract")
    option = int(input("choose option"))
    
    if option==1:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter Second Number "))
        print("Sum of {} and {} is {} ".format(num1,num2,(num1+num2)))
    elif option ==2:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter Second Number "))
        substract = num1 - num2
        print("Substraction of {} and {} is {} ".format(num1,num2,substract))
    else:
        print("Invalid Input ")