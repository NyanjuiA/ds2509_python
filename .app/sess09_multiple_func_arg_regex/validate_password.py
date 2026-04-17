# Python script to accept a password from the user and check that
# 1. It contains at least one lowercase, and one uppercase letter,
# 2. At least one number and special character [@#$%^&*_!],
# 3. It has a minimum of 8 characters and a maximum of 15 characters

# Import the regex module
import re

# Function to validate the password complexity requirements
def validate_password(password):
   """
      Validate a password against complexity requirements using regular expressions.
      :param password(str): Password to be validated.

      Examples
       --------
       >>> validate_password("StrongPass1!")
       The password "StrongPass1!" meets the password complexity requirements

       >>> validate_password("weak")
       Please use a password with at least 8 characters, contains at least one
       lowercase letter, one uppercase letter, one number, and one special character.

       Notes
       -----
       - The special characters allowed are: @ # $ % ^ * _
       - The function uses positive lookaheads in the regex pattern to enforce rules
       - Consider using getpass.getpass() for secure password input in real applications

       Regular Expression Breakdown:
       ^                         # Start of string
       (?=.*[a-z])               # At least one lowercase letter
       (?=.*[A-Z])               # At least one uppercase letter
       (?=.*[0-9])               # At least one digit
       (?=.*[@#$%^*_&])          # At least one special character
       .{8,15}                   # Minimum 8 characters total and maximum 15 characters
       $                         # End of string
      """
   pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^*_&!]).{8,15}$"

   if password is None:
      print("Please enter a password")
      return

   # Compare the user's password with the above regex pattern and display an apt message
   if re.match(pattern, password):
      print(f"The password '{password}' meets the complexity requirements.")
   else:
      print(f"Please use a password with at least 8 characters, contains at least "
            f"one lowercase letter, one uppercase letter, one number, and one special character.")

# Run the application
if __name__ == "__main__":
   # Prompt the user for their password
   password = input("Please enter a password and I'll tell you if it "
                    "meets the complexity requirements or not.\n")

   # Validate the user's password
   validate_password(password)