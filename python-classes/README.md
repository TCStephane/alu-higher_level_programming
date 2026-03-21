# Python - Classes and Objects

This project introduces Object-Oriented Programming (OOP) in Python. Through a series of incremental tasks, we build a `Square` class that grows in complexity — starting from an empty class and ending with validated attributes, properties, and formatted output.

## Learning Objectives

- What OOP is and why Python programming is awesome
- What a class, object, and instance are
- The difference between a class and an instance
- What `self` is and how the `__init__` method works
- What public, protected, and private attributes are
- How to use properties (getters and setters) the Pythonic way
- Data Abstraction, Data Encapsulation, and Information Hiding
- How to dynamically create new attributes for instances
- How Python finds the attributes of an object or class (`__dict__`)
- How to use the `getattr` function

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable and end with a new line
- All modules, classes, and functions include docstrings

## Files

| File          | Description                                                     |
|---------------|-----------------------------------------------------------------|
| `0-square.py` | Empty class `Square` that defines a square                      |
| `1-square.py` | `Square` with a private instance attribute `size`               |
| `2-square.py` | `Square` with `size` validation (type and value checks)         |
| `3-square.py` | `Square` with a public `area()` method                          |
| `4-square.py` | `Square` with property getter/setter for `size`                 |
| `5-square.py` | `Square` with `my_print()` method to print the square using `#` |
| `6-square.py` | `Square` with `position` attribute for offset printing          |

## Usage

```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
# Output:
#
#  ###
#  ###
#  ###
```

## Author

Stephane Tchatchum — [Professional GitHub](https://github.com/stephanetchatchum)
                   — [School Github](https://github.com/TCStephane)