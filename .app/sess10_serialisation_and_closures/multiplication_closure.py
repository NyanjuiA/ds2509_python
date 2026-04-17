# Python script to demonstrate the use of a closure to multiply a parameter with
# a second value.

# Define the enclosing function
def multiplier(n):
   def inner(x): # inner function
      return x * n
   return inner

# Create 2 multiplier function
triple = multiplier(3)
quadruple = multiplier(4)

# Use the above closures to tripple 5 and quadruple 8
print(f"5 tripled is: {triple(5)}")
print(f"8 quadrupled is: {quadruple(8)}")