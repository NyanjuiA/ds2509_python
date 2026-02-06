# Python script that demonstrates how to create, write and read from a file

# Import the required modules
import os # Module to enable our script to work with the OS(Operating System) and its file system

# Create a function to create and write to a file
def create_file(path,content):
   """
   Creates a file in the given path and write the specified content to the file.

   :param path(str): The path to the file to be created.
   :param content(str): The content to be written to the file.
   """
   with open(path,'w',encoding='utf-8') as f:
      f.write(content)
      print("File created and contents written successfully!")
      f.close()

# Get the current working directory
current_dir = os.getcwd()
print(f"Our current directory is:\n{current_dir}")

# Get the path to the 'files' directory/folder by going one folder up
files_directory = os.path.abspath(os.path.join(current_dir,'..','files'))
print(f"The path to the 'files' directory/folder is:\n{files_directory}")

# Specify the file path and name of the file to be created
file_path = os.path.join(files_directory,'hello.txt')
print(f"The full path to the file to be created is:\n{file_path}")

# Specify the contents/text to be written to the file
# content = input("Please enter the message to be written to the file\n")
content = "Hello 👋🏾👋🏾 from files in Python!!!\n" #emoji <window> + <.> keys

# Call/invoke the create_file() function to create and write to the file
create_file(file_path,content)