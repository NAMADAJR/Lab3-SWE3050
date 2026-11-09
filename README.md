# Geometry Calculator — SWE3050 Lab 3

A menu-driven Python command-line application for calculating geometric measurements and classifying shapes. This project is part of the SWE3050 Software Verification and Validation lab work.

## Requirements

- Python 3
- A terminal

The application uses Python's standard library only; no third-party runtime packages are required.

## Running the application

From the project root, run:

```sh
python3 main.py
```

`main.py` is the program entrypoint. It launches the interface defined in `CLInterface.py`.

The main menu offers:

```text
1. Calculate Volume
2. Calculate Surface Area
3. Calculate Length
4. Calculate Area
5. Lab 2 Calculations
0. Exit
```

Select a category, choose a calculation from its submenu, and enter the requested measurements. Option **5** opens the shape classification submenu.

- Enter `0` in a submenu to return to the main menu.
- Enter `0` in the main menu to exit.
- Press `Ctrl+C` or send end-of-input to exit cleanly.

## Available calculations

| Category | Operations |
| --- | --- |
| Volume | Cube, cylinder, one-third cylinder volume |
| Surface area | Cube, cube with one open side, cylinder with one open end, cylinder with both ends open |
| Length | Circle diameter and radius from area; circle, semicircle, and quarter-circle perimeters |
| Area | Circle, semicircle, quarter circle, square, triangle |
| Classification | Square or rectangle from length and width; equilateral, isosceles, or scalene triangle from three sides |

Semicircle and quarter-circle perimeters include their straight edges. Triangle classification checks that the supplied sides form a valid triangle.

### Input and output

- Measurements must be finite numeric values; text, infinity, and `NaN` are rejected.
- Geometry calculations accept non-negative measurements, including zero.
- Classification requires strictly positive dimensions.
- Invalid menu selections or measurements prompt you to try again.
- Numeric results are displayed to two decimal places. Results too large to represent are reported as errors.
- Use consistent units: lengths in centimetres produce areas in square centimetres and volumes in cubic centimetres. The program does not convert units.

## Project structure

```text
.
├── main.py          # Application entrypoint
├── CLInterface.py   # Menus, input validation, and calculation dispatch
├── Area/            # Area calculations
├── Classification/  # Quadrilateral and triangle classification
├── Length/          # Radius, diameter, and perimeter calculations
├── SurfaceArea/     # Surface area calculations
└── Volume/          # Volume calculations
```

## Development

Keep calculation logic in the corresponding category module and register CLI options in `CLInterface.py`. Interactive module entrypoints should use an `if __name__ == "__main__":` guard so importing a calculation does not prompt for input.

Use Ruff to lint and format Python changes. With Ruff installed:

```sh
ruff check .
ruff format .
```

Alternatively, if `uv` is available:

```sh
uv tool run ruff check .
uv tool run ruff format .
```

Testing is handled separately by the group's testing contributor.
