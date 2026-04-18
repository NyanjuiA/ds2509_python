# Python script to demonstrate working with assertions

# Fuction to divide 2 numbers and return the quotient
def divide(x, y):
   assert y != 0, "Cannot divide by zero!" # Raises an assertion error when y (denominator) is zero '0'
   return x / y

try:
   result = divide(10, 2)

   print(f"10 ÷ 2 = {result}")

   # Attempt division by zero (will result in a error)
   result = divide(10, 0)
   print(f"10 ÷ 0 = {result}")
except AssertionError as ae:
   print(f"{ae}")

# Use an assertion for post-condition check
def factorial(n):
   assert n >= 0, "Factorial is not defined for negative numbers."
   if n == 0:
      return 1
   else:
      return n * factorial(n - 1)

# Get the factorial of 5 and -3
try:
   print(f"The factorial of 5 is: {factorial(5)}") # Expected output => 120
   print(f"The factorial of -3 is: {factorial(-3)}") # Raises an AssertionError: Factorial is not defined for negative numbers.
except AssertionError as ae:
   print(f"{ae}")

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
   try:
      assert len(numbers) > 0, "Cannot calculate the average of an empty list."
      average = sum(numbers) / len(numbers)
      print(f"The average is: {average}")
   except AssertionError as ae:
      print(f"{ae}")

# Test the fumction with a non-empty and empty lists.
calculate_average([1, 2, 3, 4, 5]) # Expected output => 3
calculate_average([]) # Assertion Error: Cannot calculate the average of an empty list