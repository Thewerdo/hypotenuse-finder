import math
type=input("do you need hypotenuse or side?")
if type=="hypotenuse":
    a=eval(input("enter side a:"))
    b=eval(input("enter side b:"))
    c=math.sqrt(a**2+b**2)
    print("hypotenuse is",c)
elif type=="side":
    a=eval(input("enter hypotenuse:"))
    b=eval(input("enter side:"))
    c=math.sqrt(a**2-b**2)
    print("side is",c)
else:
    print("invalid input")