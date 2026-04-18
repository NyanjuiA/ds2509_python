# Python script to demonstrate how to handle multiple exception

try: # Code that may raise error(s)/exception(s)
   num_list = [3,5,8]
   # Try to print a number at an invalid index
   print(f"Value at index 7 is: {num_list[7]}")

   # Other possible exceptions
   num_list + 5 # TypeError as you cannot sum an integer and a list
   num_list.remove(4) # ValueError as the list doesn't contain number 4

   # Attempt integer division by zero
   quotient = 12 / 0

# Handle the above exceptions
except IndexError:
   print(f"Error: The index you tried to access is out of range.")
except TypeError:
   print(f"Error: Sorry, you can't add an integer and a list.")
except ValueError:
   print(f"Error: Sorry, the list does not contain number '4'.")
except ZeroDivisionError:
   print(f"Error: Attempted integer division by zero. Change the denominator to non-zero value.")