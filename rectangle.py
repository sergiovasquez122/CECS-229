'''

@author Sergio Vasquez
@version 08/13/2020
@file rectangle.py
'''
class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height
