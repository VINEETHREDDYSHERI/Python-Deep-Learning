def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a - b

def division(a, b):
    return a / b

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print("Addition is {}\n Subtraction is {}\n "
      "Multiplication is {}\n Division is {}".format(addition(num1, num2),
                                                     subtraction(num1, num2),
                                                     multiplication(num1, num2),
                                                     division(num1, num2)))
