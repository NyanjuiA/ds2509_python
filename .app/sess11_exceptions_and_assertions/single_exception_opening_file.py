# Python script that demonstrates handling an exception raised whe the user tries to open a non-existent file.

try: # Write the code that may raise an exception(s) here
   file = open("non-existent.bin","rb")
   content = file.read()
   print(f"File contents are:\n{content}")
except FileNotFoundError: # Handle the file error here
   print("Error, sorry the file was not found.\nPlease check the path and file name & ensure "
         "you have access permissions, then try again.")
finally:  # Resource clean up
   if 'file' in locals():
      file.close()