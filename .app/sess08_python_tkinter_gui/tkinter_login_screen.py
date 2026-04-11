# Python GUI script to demonstrate a Tkinter login window

# Import the required modules
import tkinter as tk
from tkinter import messagebox

# Define a function to authenticate the user
def login():
   # pass
   username = entry_username.get()
   password = entry_password.get()

   # Ensure/check that the user hass filled in their username and password
   if username.strip() == '' or password.strip() == '':
      tk.messagebox.showerror("Missing Username or Password",
                              "Please enter your username and password to log in.")
      return # stop further method execution

   if username.strip() == 'admin' and password.strip() == 'pas$1': # Hard-code the username and password.
      tk.messagebox.showinfo("Login Successful",
                             "Welcome back, admin!")
   else:
       tk.messagebox.showerror("Login Failed",
                               "Incorrect username or password. Please try again.")

# Function to toggle password visibility
def toggle_password():
   # pass
   if show_password_var.get():
      entry_password.config(show="")
   else:
      entry_password.config(show="*")

# Create the main window
root = tk.Tk()
root.title("Login screen")
root.geometry("320x240")
root.resizable(width=False, height=False)

# Create a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels
label_username = tk.Label(frame, text="Username: *")
label_username.grid(row=0, column=0,padx=10, pady=10, sticky='e')

label_password = tk.Label(frame, text="Password: *")
label_password.grid(row=1, column=0,padx=10, pady=10, sticky='e')

# Entry fields
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1,padx=10, pady=10)

entry_password = tk.Entry(frame,show="*")
entry_password.grid(row=1, column=1,padx=10, pady=10)

# Checkbox for showing/hiding the password
show_password_var = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(frame, text="Show Password",
                                        variable=show_password_var, command=toggle_password)
checkbox_show_password.grid(row=2, column=1,padx=10, pady=10, sticky='w')

# Login button
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=3, columnspan=2, pady=20)

# Run the application
root.mainloop()