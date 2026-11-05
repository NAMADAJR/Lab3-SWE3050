
import math

def cylinder_volume(radius, height):
    for value in (radius, height):
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Dimensions must be finite numbers.")
        if value < 0:
            raise ValueError("Dimensions cannot be negative.")

    result = math.pi * radius**2 * height
    if not math.isfinite(result):
        raise OverflowError("Result is too large.")
    return result


def main():
    try:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print(f"Volume: {cylinder_volume(r, h):.2f}")
    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
