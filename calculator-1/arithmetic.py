"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    add_num = num1 + num2

    return add_num


def subtract(num1, num2):
    
    minus_num = num1 - num2

    return minus_num
    """Return the value of num1 minus num2."""


def multiply(num1, num2):

    multi_num = num1 * num2

    return multi_num
    """Multiply the num1 by num2 and return the result."""


def divide(num1, num2):

    div_num = num1 / num2

    return div_num
    """Divide the num1 by num2, returning a floating point."""


def square(num1):

    square_num = num1 * num1
    
    return square_num
    """Return the square of num1."""


def cube(num1):

    cube_num = num1 * num1 * num1

    return cube_num
    """Return the cube of num1."""


def power(num1, num2):

    pow_num = num1 ** num2

    return pow_num
    """Raise num1 to the power of num2 and return the value."""


def mod(num1, num2):

    mod_num = num1 % num2
    
    return mod_num
    """Return the remainder of num1 / num2."""


def add_mult(num1, num2, num3):

    add_mult_num = (num1 + num2) * num3

    return add_mult_num
    """Get the sum of num1 and num2, then multiply sum with num3."""


def add_cubes(num1, num2):

    cube_add_num = num1 * num1 + num2 * num2

    return cube_add_num
    """Add the cubes of num1 and num2."""


# commit routinely
# $ git add arithmetic.py
# $ git commit -am "Completed add function"