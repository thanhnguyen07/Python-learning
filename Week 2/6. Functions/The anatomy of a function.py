# Function
def performOperation(num1 , num2 , operation):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2
        
print(performOperation(2 , 3 , "sum"))

# Named Parameters
def performOperation(num1 , num2 , operation = "sum"):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2

print(performOperation(2 , 3))
print(performOperation(2 , 3 , "multiply"))

# Args  
def performOperation(*args):
    print(args)

performOperation(1 , 2 , 3)

# kwargs
def performOperation(*args , ** kwargs):
    print(args)
    print(kwargs)

performOperation(1 , 2 , 3 , operation = "sum")