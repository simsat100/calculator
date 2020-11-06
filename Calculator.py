# this is a calculator

import math

"""
# square root of any number
x = abs(float(input()))
print("Please enter a number to calculate its square root!")
print(math.sqrt(x))

# cos
y = float(input())
print("Please enter a number to calculate its cos!")
print(math.cos(y))

# sinus
z = float(input())
print("Please enter a number to calculate its sin!")
print(math.sin(z))
"""


def les_operations(x):

    if x == 1:
        # square root of any number
        print("Please enter a number to calculate its square root!")
        x = abs(float(input()))
        print(math.sqrt(x))
    elif x == 2:
        # cos
        print("Please enter a number to calculate its cos!")
        y = float(input())
        print(math.cos(y))
    elif x == 3:
        # sinus
        print("Please enter a number to calculate its sin!")
        z = float(input())
        print(math.sin(z))
    elif x == 4:
        print("How many number do you want to add together?")
        how = int(input())
        tup = list()
        for i in range(0, how):
            print("Enter number : ")
            inp = float(input())
            tup.append(inp)
        summa = 0
        for k in range(0, how):
            summa += tup[k]
        print("Numbers entered are :")
        print(tup)
        print("Their somme is :")
        print(summa)


def calculator():
    print("What operation do you want to do?")
    print("1. Square root")
    print("2. Cos")
    print("3. Sin")
    print("4. Somme")
    y = int(input())
    answers = [1, 2, 3, 4]
    while y not in answers:
        print("Please try a number from the list!")
        y = int(input())
    x = y
    les_operations(x)


calculator()
