# The perimeter of a semicircle
def input_radius():
    r = float(input("Enter the radius of the semicircle: "))
    return r


def calculate_perimeter(r):
    perimeter = (3.14159 * r) + (2 * r)
    return perimeter


def PerimeterSemicircle():
    radius = input_radius()
    perimeter = calculate_perimeter(radius)
    print(f"The perimeter of the semicircle with radius {radius} is: {perimeter}")


if __name__ == "__main__":
    PerimeterSemicircle()
