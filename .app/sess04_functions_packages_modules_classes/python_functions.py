# This script/file demonstrates defining and calling/invoking user defined
# functions in Python

# Define a function to display a greeting message when called/invoked
def greeting():  # does not take any parameters
   print("Hello from 'greeting()' function!")  # does not return any value as well.


# Call the 'greeting()' function
greeting()


# Define a function that accepts a parameter (user's name) and greets the user
def greet_user(username):
   print("Hello %s from Python functions!" % username)


# Prompt the user for their name
name = input("Please enter your name:\n")

# Call the 'greet_user()' function and pass the user's name as parameter
greet_user(name)


# Define a function that accepts two numbers and a '+' (-> default) or 'x' operator
# to add or multiply them respectively
def add_or_multiply(first_num, second_num, operation='+'):
   """
   This function adds or multiplies two numbers depending of the operation specified.

   :param first_num(int): The first number to be used in the calculation.
   :param second_num(int): The second number to be used in the calculation.
   :param operation(str,optional): The operation to be performed on the numbers(operands). Default is '+'.
   :return int: The sum or product of two numbers.
   :raises
      None

   Examples:
      >>> add_or_multiply(1, 2)
      3
      >>> add_or_multiply(2, 2,operation = '*')
      4
      >>> add_or_multiply(8, 5,operation = 'x')
      40
      >>> add_or_multiply(2, 2,operation = '/')
      Invalid operation!\nPlease use "+" or "x"
   """
   if operation == '+':
      return first_num + second_num
   elif operation == '*' or operation == 'x':
      return first_num * second_num
   else:
      print('Invalid operation!\nPlease use "+" or "x"')
      return  # user gave us an invalid operator, we stop further execution


# Invoke the 'add_or_multiply()' function
print(f"The sum of 3 and 5 is {add_or_multiply(3, 5)}")
print("The product of %d and %d is %d" % (3, 5, add_or_multiply(3, 5, operation='*')))

# Display the documentation string of the 'add_or_multiply()' function
print(f"The documentation string of the 'add_or_multiply()' function is:"
      f"\n{add_or_multiply.__doc__}")

# Anonymous function(s)
# An anonymous/lambda function is a way to write small compact functions quickly. They are often
# used when you need a simple function for a short period and don't want to write a full function
# using the 'def' keyword
plus_five = lambda num: num + 5  # use lambda to add 5 to a number
print(f"The sum of 7 and 5 using a lambda(anonymous function) is: {plus_five(7)}")


# The same functionality above using a normal function
def add_five(num):
   return num + 5  # define a function to add 5 to the number/value passed in


# Call/invoke the add_five() function
print(f"The sum of 2 and 5 using a normal function is : {add_five(2)}")

# Anonymous/lambda function to get the difference between 2 numbers
difference = lambda num1, num2: num1 - num2

# Sample usage of the 'difference' lambda
print(f"The difference of 3 and 5 using a lambda is:{difference(3, 5)}")


# Function with variable parameters
# Define a fuction that accepts a varying number of parameters
def get_sum(*values):
   # sum = 0;
   # for value in values:
   #    sum += value
   # return sum
   """
   This function returns the sum of all the numbers/values passed in.

   Args:
      *values: Variable number of numbers/values to be summed.

   Returns:
      int or float: The sum of all the numbers/values passed in as an integer or float.

   Raises:
       TypeError: if any of the values/numbers passed is/are not numeric.

   Examples:
      >>> get_sum(1, 2, 3)
      6
      >>> get_sum(3.5,2.1,1.4)
      7.0
      >>> get_sum(1, 2,"3")
      TypeError: All values provided must be numbers/numeric values.
   """
   try:
      return sum(values)  # succint code does the same thing as the 4 lines above
   except TypeError as e:
      raise TypeError("All values provided must be numbers/numeric values.") from e


# Create a list of numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The sum of the first ten numbers is:{get_sum(*num_list)}")
nums_with_decimals = [4.5, 1.5, 2.0]
print(f"The sum of 4.5, 1.5, and 2.0 is:{get_sum(*nums_with_decimals)}")
mixed_nums = [2, 5, '7']
print(f"The sum of 2, 5,and '7' is:{get_sum(*mixed_nums)}")
