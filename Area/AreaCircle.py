# area of a circle
def input_radius():
    r = float(input("Enter the radius of the circle: "))
    return r

def calculate_area(r):
    area = 3.14159 * r * r
    return area 

def AreaCircle():
    radius = input_radius()
    area = calculate_area(radius)
    print(f"The area of the circle with radius {radius} is: {area}")
    
AreaCircle()