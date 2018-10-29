#IMPORTING MATH FUNCTIONS

#floor(x) — returns the largest integer less than or equal to x,
#ceil(x) — returns the smallest integer greater than or equal to x,
#sqrt(x) — returns the square root of x,
#log(x) — returns the natural logarithm of x,
#log(x,a) — returns the logarithm of x to base a,
#pi is the mathematical constant pi = 3,1415926..
#e — is the mathematical constant e = 2,71828..
#sin(x) returns the sine of x in radians
#cos(x) returns the cosine of x in radians
#tan(x) returns the tangent function of x
#asin(x) returns the arcsine of x in radians

# remember the rules:
# if you use "import math",
# you must call the desired function like
# math.sqrt(x)
# or
# math.cos(y)

# But if you use "from math import cos"
# this is how you call the function: 
# cos(x)
# Then, if you what to calculate a logarithm,
# you need to write "from math import log"
# and then you may call your logarithm
# with log(y) or log(z,10)

def lastDigit():
    a = int(input())
    b = a%10
    print(b)
    
def tenDigit():
    a = int(input())
    b = a//10
    c = b%10
    print(c)
    
def sum():
    a = int(input())
    b = a//100
    c = a//10
    d = c%10
    e = a%10
    print(b+e+d)
    
def fraction():
    a = float(input())
    b = a//1
    print(a-b)
    
def firstDigit():
    a = float(input())
    b = a//1
    c = a-b
    d = (c*10)//1
    e = round(d)
    print(e)
    
def carRoute():
    N = int(input())
    M = int(input())
    from math import ceil 
    print(ceil(M/N))
    
def clock():
    a = int(input())
    b = a//60
    c = a%60
    d = 0 + b
    e = 0 + c
    print(d, e)

def totalCost():
    A = int(input())
    B = int(input())
    N = int(input())
    x = A*N
    y = B/100
    z = (N*y)//1
    a = z+x
    b = ((N*y)-((N*y)//1))*100
    print(a, b)
    
def clock1():
    H = int(input())
    M = int(input())
    S = int(input())
    a = M/60
    b = S/3600
    x = a + b + H 
    y = x/12
    print(y*360)

def clock2():
    a = float(input())
    print(a % 30 *12)



