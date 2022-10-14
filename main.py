
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# static   number1 = 5  dynmic  number1 = input("enter a number")

# divide "/"  "%" 

print("Select Operation.\n")
print("1. Add\n")
print("2. Subtract\n")
print("3. Multiply\n")
print("4. Divide\n")

while True:
    choice = input("Enter choice (1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter Second number:"))

        if choice == '1':
            # result = str(num1 + num2)
            print(num1, "+", num2, "=", num1 + num2)
            # res = isinstance(result, float)
            # print(res)
            # print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)
            # print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', num1 * num2)
            # print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', num1 / num2)
            # print(num1, '/', num2, '=', divide(num1, num2))

    next_calculation = input("Do you want next calclulation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")