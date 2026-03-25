# Python - Inheritance

This project covers inheritance in Python OOP — creating subclasses, overriding methods, validating types with `isinstance`, `issubclass`, `type`, and `super`, and building a geometry class hierarchy from `BaseGeometry` to `Rectangle` to `Square`.

## Learning Objectives

- What is a superclass, baseclass, parentclass, and subclass
- How to inherit a class from another and override methods
- How to define a class with multiple base classes
- The default class every class inherits from (`object`)
- How to use `isinstance`, `issubclass`, `type`, and `super`

## Requirements

- All files interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Code follows `pycodestyle` (version 2.7.*)
- All modules, classes, and functions include docstrings

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function returning list of attributes and methods of an object |
| `1-my_list.py` | `MyList` class inheriting from `list` with `print_sorted()` |
| `2-is_same_class.py` | Check if object is exactly an instance of a class |
| `3-is_kind_of_class.py` | Check if object is instance of, or inherited from, a class |
| `4-inherits_from.py` | Check if object inherited (directly/indirectly) from a class |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with unimplemented `area()` |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator()` |
| `8-rectangle.py` | `Rectangle` inheriting from `BaseGeometry` |
| `9-rectangle.py` | Full `Rectangle` with `area()` and `__str__` |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with custom `__str__` |

## Author

Stephane Tchatchum — [GitHub](https://github.com/stephanetchatchum)
