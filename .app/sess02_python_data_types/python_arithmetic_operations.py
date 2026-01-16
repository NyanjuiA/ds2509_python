# Python script/file to demonstrate the various arithmetic operations on numeric values

# Declare and get two numbers(variables) from the user
num1 =  int(input('Enter the first number to be used in the calculation:\n '))
num2 =  int(input('Enter the second number to be used in the calculation:\n '))

# Addition: get the sum of the two numbers
sum = num1 + num2

# Difference/subraction: get the difference of the two numbers
difference = num1 - num2

# Multiplication: get the product of the two numbers
product = num1 * num2

# Division: get the quotient of the two numbers
floating_division = num1 / num2
integer_division = num1 // num2

# Modulus: get the remainder of dividing the two numbers
modulus = num1 % num2

# Exponentiation: get the first number raised by the second number
exponent = num1 ** num2

# Display the results
print(f"Addition: {num1} + {num2} = {sum}")
print(f"Subtraction: {num1} - {num2} = {difference}")
print(f"Multiplication: {num1} * {num2} = {product}")
print(f"Floating Division: {num1} / {num2} = {floating_division}")
print(f"Integer Division: {num1} // {num2} = {integer_division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponent: {num1} ** {num2} = {exponent}")