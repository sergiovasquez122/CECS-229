'''
The purpose of this program is to test the rectangle class
@author Sergio Vasquez
@version 08/13/2020
@file rectangleTest.py
'''
from rectangle import *

r1 = Rectangle(4, 40)
r2 = Rectangle(3.5, 35.9)

print("The width of the first object is:", r1.getWidth())
print("The height of the first object is:", r1.getHeight())
print("The area of the first object is:", r1.getArea())
print("The perimeter of the first object is:", r1.getPerimeter())


print("The width of the second object is:", r2.getWidth())
print("The height of the second object is:", r2.getHeight())
print("The area of the second object is:", r2.getArea())
print("The perimeter of the second object is:", r2.getPerimeter())

