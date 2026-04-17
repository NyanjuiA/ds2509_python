# Python script to demonstrate the 're' modules methods

# Import the regular expression module
import re

from sess06_comprehensions.python_map import result

print("=" * 55)
print("re.match() demonstaration")
print("=" * 55)
print("re.match() : Check for a match only at the beginning of the string."
      "\nReturns a match object if found, else None.\n")
text = "Hello World"
pattern = r"Hello"
result1 = re.match(pattern, text)
result2 = re.match(r"World", text) # Will fail since 'Hello World' doesn't start with 'World'

if result1:
   print(f"Trying to match 'Hello' at start of '{text}': found/matched")
else:
   print(f"No match found: {result1.group()}")

print(f"Trying to match 'World' at start of '{text}': {result2}")


print("=" * 55)
print("re.search() demonstaration")
print("=" * 55)
print("re.search() : Searches the entire string for the first occurrence of the pattern\n")
# text = "Hello World"
# pattern = r"Hello"

result = re.search(pattern, text)
if result:
   print(f"Match found: {result.group()} at position (starting from 0): {result.start()}")
else:
   print(f"No match found")


print("=" * 55)
print("re.findall() demonstaration")
print("=" * 55)
print("re.findall() : Returns all non-overlapping matches as a list\n")
text = "The rain in Spain falls mainly in the plain."
pattern = r"in"

result = re.findall(pattern, text)
print(f"The word '{pattern}' was found {len(result)} times as shown below.\n{result}")

# Example to extract emails from text
text = ("John said he got the following emails from the clients.  From client1, test1@email.com,"
        "from client2, testemail@ymail.com, and from client3 tes3@outlook.com")
pattern = r"\w+@\w+\.+\w+"

print(f"The emails extracted from John's text are:\n{re.findall(pattern, text)}")

print("=" * 55)
print("re.split() demonstaration")
print("=" * 55)
print("re.split() : Splits the string  whenever the pattern matches.\n")

text = "grape avocado, grape; orange apple, mango; cherry"
pattern = r"[ ,;]+"

fruits = re.split(pattern, text)
print(f"The fruits extracted from the text are:\n{fruits}")

print("=" * 55)
print("re.sub() demonstaration")
print("=" * 55)
print("re.sub() : Replaces all or a specified number of occurences of the pattern with a replacement string.\n")
text = "The price of petroleum is Kes. 216 and diesel is Kes. 209."
pattern = r"\d+"

# Replace the numbers with '***'
result = re.sub(pattern, "***", text)
print(f"The result of the number replacement is:\n{result}")

# Example with function replacement
def double_number(match):
   number = int(match.group())
   return str(number * 2)

text = "Numbers: 3 8 5 12 7"
result = re.sub(pattern, double_number, text)
print(f"The result of the double number replacement is:\n{result}")