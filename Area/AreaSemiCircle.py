# The area of a semicircle
def input_radius():
    r = float(input("Enter the radius of the semicircle: "))
    return r


def calculate_area(r):
    area = (3.14159 * r * r) / 2
    return area


def AreaSemicircle():
    radius = input_radius()
    area = calculate_area(radius)
    print(f"The area of the semicircle with radius {radius} is: {area}")


if __name__ == "__main__":
    AreaSemicircle()
