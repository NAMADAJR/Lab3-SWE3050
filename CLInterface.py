# CLI
import Volume, SurfaceArea, Length, Area, Lab2

def main():
    print("Welcome to the Geometry Calculator!")
    print("Please select an option:")
    print("1. Calculate Volume")
    print("2. Calculate Surface Area")
    print("3. Calculate Length")
    print("4. Calculate Area")
    print("5. Lab 2 Calculations")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        Volume.calculate_volume()
    elif choice == '2':
        SurfaceArea.calculate_surface_area()
    elif choice == '3':
        Length.calculate_length()
    elif choice == '4':
        Area.calculate_area()
    elif choice == '5':
        Lab2.perform_lab2_calculations()
    else:
        print("Invalid choice. Please try again.")