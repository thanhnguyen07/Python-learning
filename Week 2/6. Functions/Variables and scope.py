# Local
def performceOperation(num1 , num2 , operation = "sum"):
    print(locals())
performceOperation(1 , 2 , operation = "multiply")

# Global

# Global and Local scope
message = "Some global data"
varA = 2

def function1(varA , varB):
    print(varA)
    print(message)
    print(locals())

def function2(varC , varB):
    print(varA)
    print(message)
    print(locals())

function1(1 , 2)
function2(3 , 4)

def function1(varA , varB):
    message = "Some local message"
    print(varA)
    def inner_function(varA , varB):
        print(f"inner_function local scope: {locals()}")
    
    print(locals())
    inner_function(123 , 456)

function1(1 , 2)