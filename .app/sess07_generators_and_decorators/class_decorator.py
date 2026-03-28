# Python script to demonstrate decorating a class with a logger

# Define the logging function
def log_dimensions(cls):
   def wrapper(*args, **kwargs):
      print(f"Logging dimensions for {cls}")
      rectangle = cls(*args, **kwargs)
      print(f"Rectangle dimensions logged!")
      return rectangle

   return wrapper


@log_dimensions
class Rectangle:
   def __init__(self, width=0, length=0):
      self.width = width
      self.length = length

   def get_width(self):
      return self.width
   def set_width(self,width):
      self.width = width

   def get_length(self):
      return self.length
   def set_length(self,length):
      self.length = length

   def calculate_area(self):
      return self.width * self.length

   def calculate_perimeter(self):
      return 2 * (self.width + self.length)

   def __str__(self):
      return (
         f"Rectangle's Dimensions"
         f"\n" + "-" * 42 +
         f"\nWidth: {self.width} cm."
         f"\nLength: {self.length} cm."
         f"\nArea: {self.calculate_area()} cm²."
         f"\nPerimeter: {self.calculate_perimeter()} cm."
         f"\n" + "-" * 42
      )

# Prompt the user for the dimensions of a new Rectangle
length = int(input("Please enter the length of the rectangle in cm:\n"))
width = int(input("Please enter the width of the rectangle in cm:\n"))
# Create/instantiate a Rectangle object with the dimensions given by the user
rectangle = Rectangle(width, length)
print(rectangle)

# Create/instantiate a Rectangle using hard-coded values
rectangle2 = Rectangle(width = 5, length = 8)
print(rectangle2)
