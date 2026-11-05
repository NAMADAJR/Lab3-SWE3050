# The surface area of a cube\
def input_side_length():
    s = float(input("Enter the side length of the cube: "))
    return s

def calculate_surface_area(s):
    surface_area = 6 * s * s
    return surface_area

def SAreaCube():
    side_length = input_side_length()
    surface_area = calculate_surface_area(side_length)
    print(f"The surface area of the cube with side length {side_length} is: {surface_area}")
    
SAreaCube()