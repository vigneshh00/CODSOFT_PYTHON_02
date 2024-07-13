def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    print("------CALCULATOR------")
    while True:
        print("Select any one of the following operations\n"
              "1.Addition\n"
              "2.Subtraction\n"
              "3.Multiplication\n"
              "4.Division\n"
              "5.Exit\n")
        choice = int(input("Enter your choice (corresponding number of your operation): "))

        if choice == 5:
            print("Thank you for using our calculator!")
            exit()

        if choice >= 1 and choice <=4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = add(num1, num2)
                print(f"Addition of the two numbers is {result:.2f}\n")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Subtraction of the two numbers is {result:.2f}\n")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Multiplication of the two numbers is {result:.2f}\n")
            elif choice == 4:
                if int(num2) == 0:
                    print("Undefined operation")
                else:
                    result = divide(num1, num2)
                    print(f"Division of the two numbers is {result:.2f}\n")
        else:
            print("Invalid choice! Please enter the correct option.\n")

if __name__ == "__main__":
    calculator()