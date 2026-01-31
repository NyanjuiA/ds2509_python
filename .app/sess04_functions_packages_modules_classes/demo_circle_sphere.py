# Python script/file to demonstrate working with user-defined/custom classes
# and instatiating them

# Import the required modules
from circle import Circle
from sphere import Sphere

# Prompt the user for the circle's radius in (m,feet,cm)
radius = float(input('Please enter the radius of the circle in cm:\n'))

# Create/instantiate a Circle object
circle1 = Circle(radius)

# Display the circle's dimensions
print(circle1)

# Prompt the user for the sphere's radius in (m,feet,cm)
radius = float(input('Please enter the radius of the sphere in cm:\n'))

# Create/instantiate a Sphere object
sphere1 = Sphere(radius)

# Display the sphere's dimensions
print(sphere1)