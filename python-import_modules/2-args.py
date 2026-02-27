
import sys
if __name__ == "__main__":
    arguments = sys.args[1:]
    count = len(arguments)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for i in range(count):
        print(f"{i + 1}: {arguments[i]}")
