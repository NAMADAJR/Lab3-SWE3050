# The perimeter of a circle
def input_radius():
    r = float(input("Enter the radius of the circle: "))
    return r

def calculate_perimeter(r):
    perimeter = 2 * 3.14159 * r
    return perimeter

def PerimeterCircle():
    radius = input_radius()
    perimeter = calculate_perimeter(radius)
    print(f"The perimeter of the circle with radius {radius} is: {perimeter}")
    
PerimeterCircle()