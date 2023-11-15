def runCalc():
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    
    print("\nEnter Operation: \n 1 - Addition\n 2 - Subtraction \n 3 - Multiply \n 4 - Division \n")
    operation = int(input("Operation: "))
    
    output =0
    
    if operation == 1:
        output = addition(x,y)
    elif operation == 2:
        output = subtract(x,y)
    elif operation == 3:
        output = multiply(x,y)
    elif operation == 4:
        output = divide(x,y)
    else:
        errorHandling()
    
    if(output!=0):
        print("\nThe answer is: {}".format(output))
    
def addition(x,y):
    sum = x+y
    return sum
    
def subtract(x,y):
    difference = x-y
    return difference
    
def multiply(x,y):
    if x==0 or y==0:
        return ("Zero")
    else:
        product = x*y
        return product
                   
def divide(x,y):
    if x==0:
       return ("Error. The numerator is zero, answer is zero")
    elif y==0:
        return ("Error. The denominator is zero, answer is undefined")
    else:
        quotient = x/y
        return quotient

def errorHandling():
    print("Incorrect option.")

count =1
while count ==1:
    
    runCalc()
    
    print("\nWould you like to try again?: \n1 - Try again\n2 - Exit\n")
    count = int(input("\nDecision: "))
    