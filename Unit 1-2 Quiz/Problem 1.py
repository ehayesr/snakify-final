def squareRect():
    name = input()
    l = int(input())
    w = int(input())
    h = int(input())
    vol = ((l*w*h)/7.5)
    print(name, 'you need', vol, 'gallons.')

def cylindrical():
    from math import pi
    name = input()
    r = int(input())
    h = int(input())
    vol = (((1/3)*pi*((r)**2)*h)/5.875)
    print(name, 'you need', vol, 'gallons.')
    