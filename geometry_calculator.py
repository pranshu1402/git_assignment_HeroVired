import math

class GeometryCalculator:
    def calculate_rectangle_area(self, length, width):
        return length * width
    
    def calculate_circle_area(self, radius):
        return math.pi * (radius ** 2)


if __name__ == "__main__":
    calculator = GeometryCalculator()

    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")
    length = int(length)
    width = int(width)
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")

    radius = input("Enter the radius of the circle: ")
    radius = int(radius)
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")
