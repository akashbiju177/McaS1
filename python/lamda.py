num=int(input("Enter a number: "))
list=[i for i in  range(1,num+1) if num%i==0]
print("factors of number : ",list)
print("\n enter the length and breadth of a rectangle: ")
length=int(input("length of rectangle: "))
breadth=int(input("breadth of rectangle: "))
c= lambda x,y:x*y
print("Area of rectangle : ",c(breadth,length))
print("\n enter side of the square: ")
s=int(input("side of square: "))
l= lambda x: x*x
print("Area of square : ",l(s))