def enter_side(side):
    while True:
        try:
            return float(input(f"Enter the length of side {side}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")


def is_valid_triangle(a, b, c):
    if min(a, b, c) <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def classify_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return None
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"


def run():
    a, b, c = (enter_side(side) for side in "abc")
    result = classify_triangle(a, b, c)

    if result is None:
        print("Not a triangle")
    else:
        print(f"The triangle is: {result}")


if __name__ == "__main__":
    run()
