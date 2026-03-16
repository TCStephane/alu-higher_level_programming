#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    arr = list(roman_string)
    for i in range(len(arr)):
        prev = values[arr[i]]
        if i+1 < len(arr):
            nex = values[arr[i+1]]
        else:
            nex = 0
        if prev < nex:
            result -= prev
        else:
            result += prev
    return result
