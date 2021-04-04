import math

x = 0
period = 30.0
pi = 3.1415927

for i in range(-10,11):
    print("-", end = "")
    
print("\n", end = "")

def printLine(y):
    """Output a line, drawing the axes and the function value"""
    funcPos = round(y*10)
    for i in range(-10,11):
        if i == funcPos:
            print("*", end = "")
        elif i == 0:
             print("|", end = "")
        else:
             print(".", end = "")


while True:
    y = math.sin((2*pi/period)*x)
    x = x + 1
    printLine(y)
    print("\n", end = "")
