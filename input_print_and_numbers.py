#MATH
def math():
    print(5 + 10)
    print(7 - 3)
    print(4 * 5)
    print(5 / 3)
    print(2 ** 16)  # two stars are used for exponentiation
    print(37 / 3)  # single forward slash is a division
    print(37 // 3)  # double forward slash is an integer division
    print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder
    print(3 * 7, (17 - 2) * 8)

#SUM OF THREE NUMBERS
def sum():
    # This program reads two numbers and prints their sum:
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)
    # Can you change it so it can add three numbers?

#HI JOHN
def hiJohn():
    # Read an integer:
    # a = int(input())
    # Read a float:
    # b = float(input())
    # Print a value:
    # print(a, b)

    a = 'Hi'
    b = input()
    print(a,b)

#SQUARE
def square():
    # Read an integer:
    # a = int(input())
    # Read a float:
    # b = float(input())
    # Print a value:
    # print(a, b)
    a = int(input())
    b = a**2
    print(b)

#AREA OF A RIGHT TRIANGLE
def area():
    # Read the numbers b and h like this:
    b = int(input())
    a = int(input())
    # Print the result with print()
    print(.5 * (a*b))

#HELLO, HARRY!
def harry():
    # Read the name:
    name = input()

    # Print the result using:
    # print('Greeting', name)
    print('Hello, ' + name + '!')

#APPLE SHARING
def appleSharing():
    # Read the numbers like this:
    n = int(input())
    k = int(input())
    # Print the result with print()

    # Example of division, integer division and remainder:
    print(k // n)
    print(k % n)

#PREVIOUS AND NEXT
def previous():
    # Read an integer:
    # a = int(input())
    # Read a float:
    # b = float(input())
    # Print a value:
    # print(a, b)
    a = int(input())
    b = int(a + 1)
    c = int(a - 1)
    print('The next number for the number', a, 'is', b)
    print('The previous number for the number', a, 'is', c)

#TWO TIMESTAMPS
def timestamps():
    # Read an integer:
    # a = int(input())
    # Read a float:
    # b = float(input())
    # Print a value:
    # print(a, b)
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    x = int((d-a)*3600)
    y = int((e-b)*60)
    z = int(f-c)
    sec = int(x+y+z)
    print(sec)

#SCHOOL DESKS
def desks():
    # Read an integer:
    # a = int(input())
    # Read a float:
    # b = float(input())
    # Print a value:
    # print(a, b)
    a = int(input())
    b = int(input())
    c = int(input())
    d = int((a//2)+(a%2))
    e = int((b//2)+(b%2))
    f = int((c//2)+(c%2))
    print(d+e+f)



