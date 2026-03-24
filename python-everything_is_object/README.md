# Python - Everything is object

This project explores how Python handles objects, references, mutability, and identity. Unlike typical coding projects, most tasks are conceptual questions about Python's behavior with different object types.

## Learning Objectives

- What is an object, a reference, an assignment, and an alias
- The difference between mutable and immutable objects
- How to check if two variables are identical (`is`) vs equal (`==`)
- How to display a variable's memory address using `id()`
- Built-in mutable types: list, dict, set, bytearray
- Built-in immutable types: int, float, str, tuple, frozenset, bytes
- How Python passes variables to functions (by object reference)
- Integer caching (NSMALLPOSINTS / NSMALLNEGINTS: -5 to 256)

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Answer files contain only one line with no leading/trailing spaces
- Python scripts follow `pycodestyle` (version 2.7.*)

## Files

| File              | Answer          | Explanation |
|-------------------|-----------------|-------------|
| `0-answer.txt`    | `type`          | Function to print an object's type |
| `1-answer.txt`    | `id`            | Function to get memory address |
| `2-answer.txt`    | `No`            | 89 and 100 are different values |
| `3-answer.txt`    | `Yes`           | 89 is in CPython's integer cache (-5 to 256) |
| `4-answer.txt`    | `Yes`           | `b = a` creates an alias |
| `5-answer.txt`    | `No`            | `a + 1` creates a new object |
| `6-answer.txt`    | `True`          | `==` checks value equality |
| `7-answer.txt`    | `True`          | `s2 = s1` is an alias |
| `8-answer.txt`    | `True`          | Same string content |
| `9-answer.txt`    | `True`          | String interning |
| `10-answer.txt`   | `True`          | Same list content |
| `11-answer.txt`   | `False`         | Two separate list objects |
| `12-answer.txt`   | `True`          | Alias, same content |
| `13-answer.txt`   | `True`          | Alias, same object |
| `14-answer.txt`   | `[1, 2, 3, 4]`  | `.append()` mutates the shared list |
| `15-answer.txt`   | `[1, 2, 3]`     | `+` creates a new list |
| `16-answer.txt`   | `1`             | Integers are immutable |
| `17-answer.txt`   | `[1, 2, 3, 4]`  | Lists are mutable |
| `18-answer.txt`   | `[1, 2, 3]`     | Reassigning local variable doesn't affect original |
| `19-copy_list.py` | —               | Function that returns a copy of a list |
| `20-answer.txt`   | `Yes`           | `()` is an empty tuple |
| `21-answer.txt`   | `Yes`           | `(1, 2)` is a tuple |
| `22-answer.txt`   | `No`            | `(1)` is just an int in parentheses |
| `23-answer.txt`   | `Yes`           | `(1,)` trailing comma makes it a tuple |
| `24-answer.txt`   | `True`          | `(1)` is just `1`, cached integer |
| `25-answer.txt`   | `False`         | Two separate tuple objects |
| `26-answer.txt`   | `True`          | Empty tuple is cached by CPython |
| `27-answer.txt`   | `No`            | `a + [5]` creates a new list |
| `28-answer.txt`   | `Yes`           | `+=` on lists modifies in place |

## Author

Stephane Tchatchum — [Professional GitHub](https://github.com/stephanetchatchum)
                     [School Github](https//github.com/TCStephane)