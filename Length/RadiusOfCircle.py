# The radius of a circle, input is the area
def input_area():
    a = float(input("Enter the area of the circle: "))
    return a


def calculate_radius(a):
    radius = (a / 3.14159) ** 0.5
    return radius


def RadiusOfCircle():
    area = input_area()
    radius = calculate_radius(area)
    print(f"The radius of the circle with area {area} is: {radius}")


if __name__ == "__main__":
    RadiusOfCircle()
