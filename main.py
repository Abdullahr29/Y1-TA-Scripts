
from random import choices # Don’t worry what this means for now...
import math
import os.path
import twister
import numpy as np
import matplotlib.pyplot as plt


def fibonacci(num):
    num0 = 0
    num1 = 1
    print(num0)
    print(num1)
    for x in range(1, num):
        temp = num0 + num1
        num0 = num1
        num1 = temp
        print(num1)


def while_fibonacci():
    num0 = 0
    num1 = 1
    print(num0)
    print(num1)
    temp = num0 + num1
    while(temp < 1000000):
        temp = num0 + num1
        num0 = num1
        num1 = temp
        if(temp < 1000000):
            print(num1)

def fizzbuzz(coolNum1, coolNum2):
    for i in range(1, 101):
        if((i % coolNum1 == 0) and (i % coolNum2 == 0)):
            print("fizzbuzz!! (" + str(i) + ")")
        elif((i % coolNum1 == 0)):
            print("fizz! (" + str(i) + ")")
        elif((i % coolNum2 == 0)):
            print("buzz! (" + str(i) + ")")
        else:
            print(i)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial of", n, "is", fact)

def raise_to(num, power):
    final = 1
    for i in range(1, power+1):
        final = final*num
    return final

def add_all(*nums):
    final = 0
    for num in nums:
        final = final + num
    return final



def chop_rec(array, element, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return chop_rec(array, element, start, mid-1)
    else:
        return chop_rec(array, element, mid+1, end)

def circular():
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    xx, yy = np.meshgrid(x, y)
    z = xx*yy
    #z = np.sin(np.sqrt(xx ** 2 + yy ** 2)) / np.sqrt(xx ** 2 + yy ** 2)
    h = plt.imshow(z, origin='lower', extent=[-10, 10, -10, 10])
    plt.colorbar(h)
    plt.show()

def crest():
    Crest = plt.imread('CrestBW.png')
    plt.subplot(1, 2, 1)
    plt.imshow(Crest, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(np.fliplr(Crest), cmap='gray')
    plt.axis('off')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #spam = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    #print(spam[0:3,0:1])

    spam = np.array(range(1, 100))
    print(spam[0:-1:3])

    #X = numpy.arange(0, 6 * numpy.pi, 0.1)
    #Y = numpy.sin(X)
    #plt.plot(X, Y)
    #plt.show()
    #circular()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
