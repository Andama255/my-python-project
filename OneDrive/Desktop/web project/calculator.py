#My calculator Project PLP
num1 = float(input("Enter first numbe: "))
num2 = float(input("Enter second number: "))
operator = input("Enter preffered operation ['+','-','*','/']: ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero"
    return x / y

if operator == '+':

    result = add(num1, num2)
    print(f"result: {result}")

elif operator == '-':

    result = subtract(num1, num2)
    print(f"result: {result}")

elif operator == '*':

    result = multiplication(num1, num2)
    print(f"result: {result}")

elif operator == '/':

    result = division(num1, num2)
    print(f"result: {result}")

else:
    print("invalid option selected")                