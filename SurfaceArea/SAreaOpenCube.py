# The surface area of a cube with one open side
def input_side_length():
    s = float(input("Enter the side length of the cube: "))
    return s


def calculate_surface_area(s):
    surface_area = 5 * s * s
    return surface_area


def SAreaOpenCube():
    side_length = input_side_length()
    surface_area = calculate_surface_area(side_length)
    print(
        f"The surface area of the cube with one open side and side length {side_length} is: {surface_area}"
    )


if __name__ == "__main__":
    SAreaOpenCube()
