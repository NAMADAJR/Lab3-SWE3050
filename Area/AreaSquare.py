
import math

def square_area(side):
    if not isinstance(side, (int, float)) or not math.isfinite(side):
        raise ValueError("Side must be a finite number.")
    if side < 0:
        raise ValueError("Side cannot be negative.")

    result = side**2
    if not math.isfinite(result):
        raise OverflowError("Result is too large.")
    return result


def main():
    try:
        side = float(input("Enter side length: "))
        print(f"Area: {square_area(side):.2f}")
    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
