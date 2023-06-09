#!/usr/bin/python3

if __name__ == "__main__":

    # Import the add, sub, mul, and div functions from the calculator_1 module.
    from calculator_1 import add, sub, mul, div

    # Import the sys module.
    import sys

    # Check if the number of arguments is 3.
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get the first two arguments.
    a = int(sys.argv[1])
    operator = sys.argv[2]

    # Check if the operator is valid.
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Get the third argument.
    b = int(sys.argv[3])

    # Calculate the result.
    result = {"+": add, "-": sub, "*": mul, "/": div}[operator](a, b)

    # Print the result.
    print("{} {} {} = {}".format(a, operator, b, result))
