# Function that accepts only Non-Negative Integer from the user.
def getPositiveIntFromUser():
    n = -1
    while n < 0:  # Loops stops once n variable value is greater than zero
        try:
            n = int(input("Enter Non-Negative Integer: "))
        except ValueError:  # if the user input value is Non-Integer then error
            # gonna rise as it can't be converted to Integer
            print("Please Enter Valid Non-Negative Integer")
            n = -1
    return n


num = getPositiveIntFromUser()  # Function returns Non-Negative Integer
temp = num  # Temporary Variable to do the calculation
noOfSteps = 0
while temp != 0:  # loops runs until temp variable becomes zero
    noOfSteps += 1  # Incrementing the variable until the loop runs (i.e until the temp variable becomes zero)
    if temp % 2 == 0:  # Checking if the number is Even
        temp = temp // 2
    else:
        temp = temp - 1
print("No of Steps for the given number {} to reach zero is {}".format(num, noOfSteps))  # Printing the Output
