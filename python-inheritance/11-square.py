#!/usr/bin/python3
"""Module that defines Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with validated size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
