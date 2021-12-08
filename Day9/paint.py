# PAINT A WAll
# Return how much paint is required to paint a wall given its length and height
# Assume 1 paint box covers 5 square ms

def paint_calc(length , height , coverage):
    area = length * height
    paint = area / coverage
    print(round(paint))

height = int(input("Enter the height of the wall "))
length = int(input("Enter the length of the wall "))

coverage = 5

paint_calc(length, height, coverage)
