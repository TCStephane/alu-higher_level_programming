#!/usr/bin/python3
print("".join(["{:c}".format(i) for i in range(ord('a'), ord('z') +1 ) if i != ord('e') and i != ord('q')]), end="")
