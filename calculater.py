#create a calculater capable of performing addition, substraction, multiplication,division 
#operation on two number, you program should format the output in a readable manner!.

def myNumber(firstNumber, secondNumber):
    
    print("Enter 1 for +\nEnter 2 for -\nEnter 3 for *\nEnter 4 for // ")
    EnterNumber= int(input("Please select your number from 1 to 4:-  "))
    
    if (EnterNumber==1):
        print("Addition of your first and second number is",firstNumber + secondNumber)
    elif (EnterNumber==2):
        print("Substraction of your first and second number is",firstNumber - secondNumber)
    elif (EnterNumber==3):
        print("Multiplication of your first and second number is",firstNumber * secondNumber)
    elif (EnterNumber==4):
        print("Division of your first and second number is",firstNumber // secondNumber)
    else:
        print("invalid")
firstNumber = int(input("Enter the first number "))
if firstNumber<=0:
    print("invalid number")
secondNumber = int(input("Enter the second number "))
myNumber(firstNumber,secondNumber)




# firstNumber = int(input("Enter the first number "))

# secondNumber = int(input("Enter the second number "))

# def Myfunction(number):
#     print("Enter the valid Number")
# function(1)


