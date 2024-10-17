# Area of triangle given base and height
b = eval(input("Enter base of triangle: "))
h = eval(input("Enter height of triangle: "))
area = 1/2 * b * h
print("Area of Triangle: ", area)

# Area of triangle given three side
import math
a = eval(input("Enter three sides of a triangle: "))
b = eval(input())
c = eval(input())
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle = ",area)
