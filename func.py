def factorial(x):
    """This is an iterative function
    to find the factorial of an integer"""
    output = 1
    for factor in range(2,x+1):
        output = output * factor
    return output

print(factorial(4))
