
import math

def open_ends_cylinder_area(radius, height):
    for value in (radius, height):
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Dimensions must be finite numbers.")
        if value < 0:
            raise ValueError("Dimensions cannot be negative.")

    result = 2 * math.pi * radius * height
    if not math.isfinite(result):
        raise OverflowError("Result is too large.")
    return result


def main():
    try:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print(f"Surface Area: {open_ends_cylinder_area(r, h):.2f}")
    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
