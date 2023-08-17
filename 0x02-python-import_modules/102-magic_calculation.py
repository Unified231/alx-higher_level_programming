#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = a + b
        for i in range(4, 6):
            c = c + i
        return c

    else:
        return a - b
