# Python script to demonstrate the use of formal, positional and keyword arguments
# in a function

# Function definition
def profile(name, *args, **kwargs):
   print(f"Name: {name}") # Formal argument
   if args: # Positional variable argument(s)
      print(f"Hobbies: ")
      for hobby in args:
         print(f"- {hobby}")

   if kwargs: # Keyword variable argument(s)
      print(f"Other info. :")
      for key, value in kwargs.items():
         print(f"- {key}: {value}")

# Function call/invocation
profile("Nyanjui", "Reading, Travelling, Cooking, Basketball", gender="Male",age=16,
        job="IT Lecturer", city="Mombasa", county="Kiambu",country="Kenya")

# NB:
# 1. Formal arguments :- are defined in the function signature(name in profile function)
# 2. *args  :- collects positional arguments as a tuple
# 3. **kwargs :- collects keyword arguments as a dictionary