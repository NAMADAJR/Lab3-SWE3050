
import math

def triangle_area(base, height):
    for value in (base, height):
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError("Dimensions must be finite numbers.")
        if value < 0:
            raise ValueError("Dimensions cannot be negative.")

    result = 0.5 * base * height
    if not math.isfinite(result):
        raise OverflowError("Result is too large.")
    return result


def main():
    try:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area: {triangle_area(b, h):.2f}")
    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
