#<: less — the condition is true if left side is less than right side. 

#>: greater — the condition is true if left side is greater than right side. 

#<=: less or equal.

#>=: greater or equal.

#==: equal.

#!=: not equal. 

#use bool() to cast input data to true or false

#Operator and is the binary operator which evaluates to True if and only if both its left-hand side and right-hand side are True.

#Operator or is the binary operator which evaluates to True if at least one of its sides is True.

#Operator not is the unary negation. It's evaluated to True if the input value is False, and, vice versa, it evaluates to false if the input value is true.

#If you have more than two options using the conditional operator, you can use if... elif... else statement.

def minimum2():
    a = int(input())
    b = int(input())
    if a<b:
        print(a)
    else:
        print(b)

def sign():
    a = int(input())
    if a > 0:
        print(1)
    elif a == 0:
        print(0)
    else:
        print(-1)

def minimum3():
    a = int(input())
    b = int(input())
    c = int(input())
    if a < b and a < c:
        print(a)
    elif b < a and b <c:
        print(b)
    else:
        print(c)

def equalNumbers():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b and a == c:
        print(3)
    elif a == b or a == c or b == c:
        print(2)
    else:
        print(0)

def rook():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if abs(a - c) <= 7and b - d == 0:
        print('YES')
    elif abs(b - d) <= 7 and a - c == 0:
        print('YES')
    else:
        print('NO')

def chess():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if (a + b) % 2 == 0 and (c+d) % 2 == 0:
        print('YES')
    elif (a + b) % 2 != 0 and (c+d) % 2 != 0:
        print('YES')
    else:
        print('NO')

def king():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if abs(a-c) == 1 and abs(b-d) == 1:
        print('YES')
    elif abs(a-c) == 1 and abs(b-d) == 0:
        print('YES')
    elif abs(a-c) == 0 and abs(b-d) == 1:
        print('YES')
    else:
        print('NO')

def bishop():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if abs(a - c) == abs(b - d):
        print('YES')
    else:
        print('NO')

def queen():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if abs(a-c) == abs(b - d):
        print('YES')
    elif a == c:
        print('YES')
    elif b == d:
        print('YES')
    else:
        print('NO')

def knight():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = abs(a - c)
    f = abs(b - d)
    if e == 1 and f == 2:
        print('YES')
    elif e == 2 and f == 1:
        print('YES')
    else:
        print('NO')

def chocolate():
    n = int(input())
    m = int(input())
    k = int(input())
    if k < n * m and (k % n == 0):
        print('YES')
    elif k < n * m and (k % m == 0):
        print('YES')
    else:
        print('NO')

def leapYear():
    a = int(input())
    if (a % 4 == 0) and (a % 100 != 0):
        print('LEAP')
    elif (a % 4 == 0) and (a % 400 == 0):
        print('LEAP')
    else:
        print('COMMON')