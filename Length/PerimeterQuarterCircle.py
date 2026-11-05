# The perimeter of a ¼ of a circle.
def input_radius():
    r = float(input("Enter the radius of the quarter circle: "))
    return r

def calculate_perimeter(r):
    perimeter = (3.14159 * r / 2) + (2 * r)
    return perimeter

def PerimeterQuarterCircle():
    radius = input_radius()
    perimeter = calculate_perimeter(radius)
    print(f"The perimeter of the quarter circle with radius {radius} is: {perimeter}")
    
PerimeterQuarterCircle()