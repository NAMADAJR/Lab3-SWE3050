# The diameter of a circle, input is the area
def input_area():
    a = float(input("Enter the area of the circle: "))
    return a


def calculate_diameter(a):
    radius = (a / 3.14159) ** 0.5
    diameter = radius * 2
    return diameter


def DiameterCircle():
    area = input_area()
    diameter = calculate_diameter(area)
    print(f"The diameter of the circle with area {area} is: {diameter}")


if __name__ == "__main__":
    DiameterCircle()
