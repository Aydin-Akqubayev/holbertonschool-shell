#!/usr/bin/python3
"""Importing the Rectangle class and creating an instance. """

class Rectangle:
    """Representing a rectangle with width and height. """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
        