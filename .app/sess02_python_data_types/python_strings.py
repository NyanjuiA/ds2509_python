#  Python script/file to demonstrate working with strings

# Declare a string variable
string_var = "hello Nyanjui from Python programming"

# Display the above string with the first letter in uppercase using % and an f-string
print("'string_var' with the first letter capitalised is: %s." % string_var.capitalize())
print(f"'string_var' with the first letter capitalised is: {string_var.capitalize()}.")

# Display the type of 'string_var'
print(f'The type of "string_var" is: {type(string_var)}')

# Display the contents of 'string_var' in upper case using .upper()
print(f"The contents of 'string_var' in upper case are: {string_var.upper()}")

# Display the contents of 'string_var' in lower case using .lower()
print(f"The contents of 'string_var' in lower case are: {string_var.lower()}")

string_2_center = "Programming"
# Center the above text with a specified width and given fill character
print(string_2_center.center(30,'*'))
# print(string_2_center.center(30,'*'))

# Display the number of times a particular character 'o' appears in 'string_var' using the .count() function
print(f"The letter 'o' appears {string_var.count('o')} times in the 'string_var' string variable.")

# Display the highest and lowest alphabetical characters in 'string_var'
print("The highest and lowest alphabetical characters in 'string_var' are"
      " '%s' & '%s' respectively!" %(max(string_var),min(string_var)))
print(f"The highest and lowest alphabetical characters in 'string_var' are"
      f" '{max(string_var)}' & '{min(string_var)}' respectively!" )

# Replace the 'hello' with 'Hallo' and 'Python' with 'C#'
new_str = string_var.replace('hello','Hallo')
# new_str = string_var.replace('hello','Hallo')
new_str = new_str.replace('Python','C#')
# Display the replace string
print("Modified contents of 'string_var' are: " + new_str)

# Declare another string variable for more string operations
my_string = "   Hello, World! 123   "

# len() - Gives/returns the no. of characters (length) in a string
print(f"Length of the string 'my_string' is: {len(my_string)} characters.")

# isalnum() - Checks if all characters are alphanumeric (no space, symbols)
print(f"Is the string  \n'{my_string}' alphanumeric? {my_string.isalnum()}")

# islower() - Checks if all alphabetic characters are lowercase
print(f"Is the string \n'{my_string}' all lowercase? {my_string.islower()}")

# isupper() - Checks if all alphabetic characters are uppercase
print(f"Is the string \n'{my_string}' all uppercase? {my_string.isupper()}")

# lstrip() - Removes any leading whitespaces (from the left side of the string/text)
print(f"Remove the leading spaces from {my_string} to get\n{my_string.lstrip()}")

# rstrip() - Removes any trailing whitespaces (from the right side of the string/text)
print(f"Remove the trailing spaces from {my_string} to get\n{my_string.rstrip()}")

# strip() - Removes any leading and trailing whitespaces (from the left and right sides of the string/text)
print(f"Remove the leading and trailing spaces from {my_string} to get\n{my_string.strip()}")

# endswith() - Check if the string ends with the specified substring
print(f"Does the string '{my_string}' end with '123  '? {my_string.endswith('123   ')}")

# endswith() - check if the string ends with the specified substring
print(f"Does the string '{my_string} end with '123'? {my_string.strip().endswith('123')}")

# startswith() - Checks if the string starts with the specified substring
print(f"Does the string '{my_string} start with '   Hello'? {my_string.startswith('Hello')}")

# startswith() - check if the string ends with the specified substring
print(f"Does the string '{my_string} start with 'Hello'? {my_string.strip().startswith('123')}")

# find() - Locates the first occurence of the specified substring
print(f"The first occurence of the string 'World' in {my_string} is at index"
      f": {my_string.find('World')}") # returns -1 when the substring is not foun

# index() - Finds the first occurence of the specified substring, raises an error when substring is not found
print("Index of 'World' in %s is at index %d" % (my_string, my_string.index("World")))

# count() - Counts the number of occurences of the substring
print("The number of occurences of 'l' in %s is %d." % (my_string, my_string.count("l")))

# rfind() - Finds the last occurence of the specified substring
print(f"The last occurence of 'l' in {my_string} is at index {my_string.rfind('l')}")

# rindex() - Finds the last occurence of the specified substring, raises an error when substring not found
print("The last index of 'l' in %s is at index %d" % (my_string, my_string.rfind('l')))



