# Python file to demonstrate the 'reduce()' function

# Import the 'reduce()' function from the functools module
from functools import reduce

# A list of numbers to be manipulated using the 'reduce()' function
numbers = [17, 45, 23, 68, 9]

# Get the largest number from the numbers list using the 'reduce()' function
largest_num = reduce(lambda x, y:max(x, y), numbers)

# Get the least number from the numbers list using the 'reduce()' function
least_num = reduce(lambda x, y:min(x, y), numbers)

# Obtain the product of the numbers in the list using the 'reduce()' function
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# Display the results
print(f"The list of numbers is:\n{numbers}")
print(f"The largest number is: {largest_num}")
print(f"The least number is: {least_num}")
print(f"The product of numbers is: {product_of_numbers}")

