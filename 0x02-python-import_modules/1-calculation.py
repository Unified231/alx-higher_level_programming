#!/usr/bin/python3

if __name__ == "__main__":

    # Import the add, sub, mul, and div functions from the calculator_1 module.
    from calculator_1 import add, sub, mul, div

    # Define two variables to store the numbers 10 and 5.
    a = 10
    b = 5

    # Calculate the sum, difference, product, and quotient of 10 and 5.
    sum = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)

    # Print the results.
    print(f"The sum of 10 and 5 is {sum}.")
    print(f"The difference of 10 and 5 is {difference}.")
    print(f"The product of 10 and 5 is {product}.")
    print(f"The quotient of 10 and 5 is {quotient}.")
