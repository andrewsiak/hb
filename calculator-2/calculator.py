"""CLI application for a prefix-notation calculator."""

# from arithmetic import (add, subtract, multiply, divide, square, cube,
#                         power, mod, )
from arithmetic import *

while True:


    calc_input = input("Enter your equation here: ")
    tokens = calc_input.split(" ")
    

    if "q" in tokens or "quit" in tokens:
        print("This is the end.")
        break

    operator = tokens[0]
    num1 = tokens[1]

    num_list = tokens[1:]
    for num in num_list:
        if not num.isdigit():
            print("Please give a number")
            continue
    # print(num_list)

    # for num in num_list:
    #     num = float(num)



# within tokens is the items; operator, num1-3
# input [+,1,2]
# equation list
    num1_only = ["square", "cube"]

  

    if not operator in num1_only:   
        num2 = tokens[2]

    

# finding number only



    if operator == "+":
        result = add(float(num1), float(num2))

    if operator == "-":
        result = subtract(float(num1), float(num2))

    if operator == "*":
        result = multiply(float(num1), float(num2))

    if operator == "/":
        result = divide(float(num1), float(num2))

    if operator == "square":
        result = square(float(num1))

    if operator == "cube":
        result = cube(float(num1))

    if operator == "pow":
        result = power(float(num1), float(num2))

    if operator == "mod":
        result = mod(float(num1), float(num2))

    if operator == "x+":
        result = add_mult(float(num1), float(num2), float(num3))

    if operator == "cubes+":
        result = add_cubes(float(num1), float(num2))


    print(result)