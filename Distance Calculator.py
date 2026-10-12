#Input
import math

# Ask the user to enter the coordinates of the first point
x1 = float(input("Point 1: "))
y1 = float(input("Point 2: "))

# Ask the user to enter the coordinates of the second point
x2 = float(input("Point 3: "))
y2 = float(input("Point 4: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result rounded to two decimal places
print(f"The distance between the two points is: {distance:.2f}")

#Output
Point 1: 1
Point 2: 2
Point 3: 3
Point 4: 4
The distance between the two points is: 2.83


>>> Program Terminated 
