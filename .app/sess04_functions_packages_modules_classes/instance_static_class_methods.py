# Python script/file to demonstrate the use of instance, static and class methods
# in a real world scenario

# import the regular expressions module
import re

# Your password must be 8 or more characters, have at least 1 lowercase, 1 uppercase, 1 number, and a
# special character

class BankAccount:
   # Class attribute (shared across all instances)
   interest_rate = 0.05 # 5% annual interest rate

   # constructor
   def __init__(self, account_holder, balance = 0.0):
      self.account_holder = account_holder
      self.balance = balance

   # ----------------------------------------------------------
   # Instance Method(s)
   # ----------------------------------------------------------
   def deposit(self, amount):
      if amount > 0:
         self.balance += amount
         # Display the new balance
         print(f"[{self.account_holder}] deposited Kes. {amount:.2f}."
               f"\nNew balance: {self.balance:.2f}")

      else:
         print(f"Kindly note that the deposit amount must be positive!")

   def withdraw(self, amount):
      if amount > 0 and self.balance >= amount: # can be shortened to [if 0 < amount <= self.balance:]
         self.balance -= amount  # to make it more realistic deduct relevant bank charges
         # Display the amount withdrawn and new balance
         print(f"[{self.account_holder}] withdrew Kes. {amount:.2f}."
               f"\nNew balance is Kes. {self.balance:.2f}")
      else:
         print(f"Invalid withdrawal amount or insufficient funds.")

   # ----------------------------------------------------------
   # Class Method(s)
   # ----------------------------------------------------------
   @classmethod
   def set_interest_rate(cls, new_rate):
      if 0 < new_rate < .2:
         cls.interest_rate = new_rate
         # Notify about the change in annual interest rate
         print(f"The annual interest rate has been set to {new_rate * 100:.2f}% for all accounts.")
      else:
         print(f"The annual interest rate must be between 0.0% and 20.0%!")

   # ----------------------------------------------------------
   # Static Method(s)
   # ----------------------------------------------------------
   @staticmethod
   def validate_account_number(account_number):
      pattern = r"^ACC\d{6}$" # Regular expression (regex) pattern to ensure the account starts
      # with 'ACC followed by 6 numbers/digits.
      return bool(re.match(pattern, account_number))

# ------------------------------------------------------------------------------
# Demonstrate the BankAccount class and its static, instance and class methods.
# ------------------------------------------------------------------------------

# Create 2 bank accounts => using the constructor
abigail_acc = BankAccount("ABIGIAL", 55000.0)
brian_acc = BankAccount("BRIAN", 10000.0)

# Deposit and withdraw money into and from the accounts => using the instance methods
abigail_acc.deposit(1500)
brian_acc.withdraw(700)

# Update the annual interest rate from 5% to 8% => using the class method
BankAccount.set_interest_rate(.08)

# Validate new account numbers => static method
print("Validating new account numbers...\nPlease wait...")
print(f"ACC123457 is valid? {BankAccount.validate_account_number('ACC123457')}")
print("Account321547 is valid?", BankAccount.validate_account_number('Account321547'))

