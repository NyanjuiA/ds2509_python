# Python script to create a simple tkinter calculator for addition, multiplication,
# subtraction, and division.

# import the required modules
import tkinter as tk
from tkinter import messagebox, ttk # ttk is for the combobox

# Define a function to read in the values from the user
def calc():
   # Get the numbers and operation from the entry fields and combobox respectively
   first_number = entry_first.get()
   second_number = entry_second.get()
   operation = entry_operation.get()

   # Check if any of the above fields are empty
   if not first_number.strip() or not second_number.strip() or not operation.strip():
      messagebox.showerror("Missing Values or Operation",
                           "Please enter all values and select the arithmetic operation")
      return # Stop further method execution

   try:
      # Convert the values from the input fields to numbers
      first_number = int(first_number)
      second_number = int(second_number)
   except ValueError:
      # Handle non-integer input
      messagebox.showerror("Invalid Values",
                           "Please enter valid numeric values for first & second number.")
      return # Stop further method execution

   # Check for division by zero
   if operation == '/' and second_number == 0:
      messagebox.showerror("Divide by Zero Error",
                           "Cannot divide by Zero '0'. Please enter a non-zero denominator.")
      return  # Stop further method execution

   # Define the arithmetic operator mappings
   # operations = \
   #    {
   #       '+': first_number + second_number,
   #       'x': first_number * second_number,
   #       '-': first_number - second_number,
   #       '/': first_number / second_number,
   #    }
   # Check whether the operation is valid and show the result
   # if operation in operations:
   #    result = operations[operation]
   #    label_answer.config(text=f"result:\t{result}")
   # else:
   #    messagebox.showerror("Invalid Operation",
   #                         "Please select a valid operation (+, -, x or /).")

   match operation:
      case '+':
         result = first_number + second_number
      case 'x':
         result = first_number * second_number
      case '-':
         result = first_number - second_number
      case '/':
         result = first_number / second_number
      case _:
         messagebox.showerror("Invalid Operation",
                              "Please select a valid operation (+, -, x or /).")
         return # Stop further function execution
   label_answer.config(text=f"Result :\t{result}")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("640x480")
root.resizable(False, False)

# Create a centered frame
frame = tk.Frame(root)
frame.place(relx=.5, rely=.5, anchor='center')

# Label widgets
label_first = tk.Label(frame, text="First Number :")
label_first.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_operation = tk.Label(frame, text="Operation(+, -, x or /) :")
label_operation.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_second = tk.Label(frame, text="Second Number :")
label_second.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_answer = tk.Label(frame, text="Answer/Result :")
label_answer.grid(row=3, column=0, padx=10, pady=10, sticky='e')

# Specify the width for the input/entry widgets
input_width = 25 # Same width for all input controls/widgets

# Entry widgets and combobox
entry_first = tk.Entry(frame, width=input_width)
entry_first.grid(row=0, column=1, padx=10, pady=10)
entry_first.insert(0, "Enter first number") # Placeholder text
entry_first.focus() # Set focus/blinking cursor or insertion point on this control

# Dropdown combobox for the desired arithmetic operation
operation_choices = ['+', '-', 'x', '/'] # List of arithmetic operations for the combobox
entry_operation = ttk.Combobox(frame, values=operation_choices, state='readonly',width=input_width-3)
entry_operation.grid(row=1, column=1, padx=10, pady=10)
entry_operation.set("Select operation") # Default value for the combobox/dropdown list

entry_second = tk.Entry(frame, width=input_width)
entry_second.grid(row=2, column=1, padx=10, pady=10)
entry_second.insert(0, "Enter second number") # Placeholder text

# Submit/Calculate button
button_calc = tk.Button(frame, text="Calculate", command=calc)
button_calc.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
