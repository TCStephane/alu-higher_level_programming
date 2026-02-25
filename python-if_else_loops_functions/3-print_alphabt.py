#!/usr/bin/python3
output = "".join(
    "{:c}".format(i) for i in range(ord('a'), ord('z') + 1)
    if i not in (ord('e'), ord('q'))
)
print(output, end="")
