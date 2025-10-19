#!/usr/bin/python3
"""
Module: polymorphism_demo
Demonstrates polymorphism and method overriding in Python.
"""

import math


class Shape:
    """Base class for different shapes."""
    def area(self):
        """Raises an error if not implemented by subclass."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
