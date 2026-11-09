# CLI
import math

from Area.AreaCircle import calculate_area as circle_area
from Area.AreaQuarterCircle import calculate_area as quarter_circle_area
from Area.AreaSemiCircle import calculate_area as semicircle_area
from Area.AreaSquare import square_area
from Area.AreaTriangle import triangle_area
from Classification.Quadrilateral import which_quadrilateral
from Classification.WhichTriangle import classify_triangle
from Length.DiameterCircle import calculate_diameter
from Length.PerimeterCircle import calculate_perimeter as circle_perimeter
from Length.PerimeterQuarterCircle import (
    calculate_perimeter as quarter_circle_perimeter,
)
from Length.PerimeterSemiCircle import calculate_perimeter as semicircle_perimeter
from Length.RadiusOfCircle import calculate_radius
from SurfaceArea.SA2SidesOpenCylinder import open_ends_cylinder_area
from SurfaceArea.SAOpenCylinder import open_cylinder_area
from SurfaceArea.SAreaCube import calculate_surface_area as cube_surface_area
from SurfaceArea.SAreaOpenCube import calculate_surface_area as open_cube_surface_area
from Volume.ThirdVolumeCylinder import third_cylinder_volume
from Volume.VolumeCube import cube_volume
from Volume.VolumeCylinder import cylinder_volume

# Each entry contains the menu label, calculation function, and required inputs.
CALCULATIONS = {
    "1": (
        "Volume",
        [
            ("Cube", cube_volume, ("side length",)),
            ("Cylinder", cylinder_volume, ("radius", "height")),
            ("One-third cylinder", third_cylinder_volume, ("radius", "height")),
        ],
    ),
    "2": (
        "Surface Area",
        [
            ("Cube", cube_surface_area, ("side length",)),
            ("Cube with one open side", open_cube_surface_area, ("side length",)),
            ("Cylinder with one open end", open_cylinder_area, ("radius", "height")),
            (
                "Cylinder with both ends open",
                open_ends_cylinder_area,
                ("radius", "height"),
            ),
        ],
    ),
    "3": (
        "Length",
        [
            ("Circle diameter from area", calculate_diameter, ("area",)),
            ("Circle radius from area", calculate_radius, ("area",)),
            ("Circle perimeter", circle_perimeter, ("radius",)),
            ("Semicircle perimeter", semicircle_perimeter, ("radius",)),
            ("Quarter-circle perimeter", quarter_circle_perimeter, ("radius",)),
        ],
    ),
    "4": (
        "Area",
        [
            ("Circle", circle_area, ("radius",)),
            ("Semicircle", semicircle_area, ("radius",)),
            ("Quarter circle", quarter_circle_area, ("radius",)),
            ("Square", square_area, ("side length",)),
            ("Triangle", triangle_area, ("base", "height")),
        ],
    ),
    "5": (
        "Classification",
        [
            ("Classify quadrilateral", which_quadrilateral, ("length", "width")),
            ("Classify triangle", classify_triangle, ("side a", "side b", "side c")),
        ],
    ),
}


def input_number(label, positive=False):
    while True:
        try:
            value = float(input(f"Enter {label}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if not math.isfinite(value):
            print("Please enter a finite number.")
        elif value < 0 or (positive and value == 0):
            requirement = "positive" if positive else "non-negative"
            print(f"Please enter a {requirement} number.")
        else:
            return value


def calculation_menu(category):
    title, options = CALCULATIONS[category]
    while True:
        print(f"\n{title}")
        for number, (label, _, _) in enumerate(options, start=1):
            print(f"{number}. {label}")
        print("0. Back to main menu")
        choice = input(f"Enter your choice (0-{len(options)}): ").strip()
        if choice == "0":
            return
        if choice not in {str(number) for number in range(1, len(options) + 1)}:
            print("Invalid choice. Please try again.")
            continue

        label, calculate, inputs = options[int(choice) - 1]
        values = [input_number(name, positive=category == "5") for name in inputs]
        try:
            result = calculate(*values)
            if result is None:
                print("Not a triangle.")
            elif isinstance(result, str):
                print(f"{label}: {result}")
            elif not math.isfinite(result):
                print("Error: Result is too large.")
            else:
                print(f"{label} — {title}: {result:.2f}")
        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")


def main():
    print("Welcome to the Geometry Calculator!")
    try:
        while True:
            print("\nPlease select an option:")
            print("1. Calculate Volume")
            print("2. Calculate Surface Area")
            print("3. Calculate Length")
            print("4. Calculate Area")
            print("5. Lab 2 Calculations")
            print("0. Exit")
            choice = input("Enter your choice (0-5): ").strip()
            if choice == "0":
                break
            if choice in CALCULATIONS:
                calculation_menu(choice)
            else:
                print("Invalid choice. Please try again.")
    except (EOFError, KeyboardInterrupt):
        print()
    print("Goodbye!")
