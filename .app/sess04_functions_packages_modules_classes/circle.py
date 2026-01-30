# Python file/script to define a 'Circle' class

# Import  the in-built math module
import math # This allows us to use/access the in-built value of pi and pow() function

class Circle:
   def __init__(self, radius = 0): # creates a Circle with a default radius of 0.
      self.radius = radius

   def calc_area(self):
      # return math.pi * self.radius ** 2 # Same as code below
      return math.pi * math.pow(self.radius, 2)

   def calc_circumference(self):
      return math.pi * (self.radius * 2)

   def __str__(self): # dunder method (double underscore)
      return (f"Circle's Dimensions"
              f"\n" + "-" * 40 +
              f"\nRadius: {self.radius} cm."
              f"\nArea: {self.calc_area():.2f} cm^2."
              f"\nCircumference: {self.calc_circumference():.2f} cm." 
              f"\n" + "-" * 40)