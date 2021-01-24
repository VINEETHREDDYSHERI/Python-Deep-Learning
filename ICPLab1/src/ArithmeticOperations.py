# Function definitions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

# Taking input from the User and then converting it from string into Integer type
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Calling that functions which perform basic arithmetic operations and printing the results
print("Addition is {}\n Subtraction is {}\n "
      "Multiplication is {}\n Division is {}".format(addition(num1, num2),
                                                     subtraction(num1, num2),
                                                     multiplication(num1, num2),
                                                     division(num1, num2)))
