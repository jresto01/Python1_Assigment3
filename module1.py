from math import pi

def get_square_footage(width, length):
    area = length * width
    print(f"The square footage is: {area} square units.")

def get_circumference(radius):
    circumference = 2 * pi * radius
    circumference = round(circumference, 4)
    print(f"The circumference is: {circumference}")