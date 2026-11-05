#!/usr/bin/env python3
import sys
def check_if_valid_number(number: str) -> float:
    try:
        num = float(number)
    except ValueError:
        print("Invalid number")
        sys.exit(1)
    if num <= 0:
        print("Number must be positive")
        sys.exit(1)
    return num


def which_quadrilateral(length: float, width: float) -> str:
    if length == width:
        return "Square"
    else:
        return "Rectangle"


def main():
    length = check_if_valid_number(input("Enter the length: "))
    width = check_if_valid_number(input("Enter the width: "))
    quadrilateral = which_quadrilateral(length, width)
    print(f"The quadrilateral is a {quadrilateral}.")



    main()
