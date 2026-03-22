# Python - More Classes and Objects

This project deepens understanding of Object-Oriented Programming (OOP) in Python by building a `Rectangle` class through 10 incremental tasks. Each task introduces a new concept — from basic properties to class methods, static methods, and special methods like `__str__`, `__repr__`, and `__del__`.

## Learning Objectives

- What is OOP and "first-class everything"
- What a class, object, and instance are
- Public, protected, and private attributes
- The `self` parameter and the `__init__` method
- Data Abstraction, Data Encapsulation, and Information Hiding
- Properties: the Pythonic way to write getters and setters
- The `__str__` and `__repr__` special methods and how they differ
- The `__del__` destructor method
- Class attributes vs instance attributes
- Class methods (`@classmethod`) and static methods (`@staticmethod`)
- How Python finds attributes using `__dict__`
- How to use the `getattr` function

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable and end with a new line
- All modules, classes, and functions include docstrings

## Files

| File | Description |
|------|-------------|
| `0-rectangle.py` | Empty class `Rectangle` |
| `1-rectangle.py` | `Rectangle` with private `width` and `height` properties |
| `2-rectangle.py` | Adds `area()` and `perimeter()` methods |
| `3-rectangle.py` | Adds `__str__` to print the rectangle with `#` |
| `4-rectangle.py` | Adds `__repr__` for eval()-compatible string representation |
| `5-rectangle.py` | Adds `__del__` destructor with farewell message |
| `6-rectangle.py` | Adds `number_of_instances` class attribute counter |
| `7-rectangle.py` | Adds `print_symbol` class attribute for customizable display |
| `8-rectangle.py` | Adds `bigger_or_equal()` static method for comparison |
| `9-rectangle.py` | Adds `square()` class method as a factory for square rectangles |

## Usage

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
# Output:
# Area: 25 - Perimeter: 20
# #####
# #####
# #####
# #####
# #####
```

## Author

Stephane Tchatchum — [GitHub](https://github.com/stephanetchatchum)
                   — [School Github](https://github.com/TCStephane)