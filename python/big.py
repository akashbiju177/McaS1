pi=3.1416
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2 and num1>num3:
    n=num1
    if num2>num1 and num2>num3:
        n=num2
    else:
        n=num3
        print(f"the biggest number is {n}")
        nn=n**2
        nnn=n**3
        result=n+nn+nnn
        print(f"n+nn+nnn={n}+{nn}+{nnn}={result}")
        radius=n
        area=pi*radius**2
        perimeter=2*pi*radius
        print(f"for a circle with radius {radius}:")
        print(f"area={area:.2f}")
        print(f"circumference={perimeter:.2f}")

