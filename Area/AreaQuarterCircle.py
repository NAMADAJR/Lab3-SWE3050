# 1/4 the area of a circle
def input_radius():
    r = float(input("Enter the radius of the quarter circle: "))
    return r


def calculate_area(r):
    area = (3.14159 * r * r) / 4
    return area


def AreaQuarterCircle():
    radius = input_radius()
    area = calculate_area(radius)
    print(f"The area of the quarter circle with radius {radius} is: {area}")


if __name__ == "__main__":
    AreaQuarterCircle()
