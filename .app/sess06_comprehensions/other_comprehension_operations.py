# Python file to demonstrate other uses of comprehensions

# List of Fibonacci numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display the squares of the above Fibonaccy numbers using a list comprehension
squares = [x ** 2 for x in numbers]
print(f"Fibonacci numbers:\n{numbers}\nFibonacci squares:\n{squares}")

# Get and display only the even Fibonacci numbers
even_fibonacci = [number for number in numbers if number % 2 == 0]
print(f"Even Fibonacci numbers:\n{even_fibonacci}")

# Dictionary of students and their mean scores in an exam
student_scores = {'Sue':56, 'Jim': 72, 'Mark':47, 'Micha':55, 'William':78,
                  'Jane':51, 'Xi':48, 'Abigail':92}
# Display the students and their scores
print(f"Students and their exam scores:\n{student_scores}")

# Get and display a dictionary of students who passed (passmark: 55)
passed_students = {name:score for name, score in student_scores.items() if score >= 55}
print(f"Students that passed and their exam scores (passmark >= 55):\n{passed_students}")

# TODO: Get and display the dictionary of students that failed

# Extract and display the set of student names from the 'student_scores' dictionary keys
student_names = set(student_scores.keys())
print(f"Student Names:\n{student_names}")

# Get a new set of student names with 4 or more characters
names_with4_or_more = {name for name in student_names if len(name) >= 5}
print(f"Student names with at for letters:\n{names_with4_or_more}")

# Comprehension with string functions
paragraph = """
To change the way a picture fits in your document, click it and a button for layout 
options appears next to it. When you work on a table, click where you want to add a 
row or a column, and then click the plus sign. Reading is easier, too, in the new 
Reading view. You can collapse parts of the document and focus on the text you want. 
If you need to stop reading before you reach the end, Word remembers where you left 
off - even on another device. Video provides a powerful way to help you prove your 
point. When you click Online Video, you can paste in the embed code for the video 
you want to add. You can also type a keyword to search online for the video that 
best fits your document.
"""

# Remove all the \n => newline characters and replace them with a space ' '
cleaned_paragraph = paragraph.replace("\n", " ")

# Split the above paragraph into sentences using the 'split()' function
sentences = cleaned_paragraph.split('.')

# Display each sentence on a new line
for sentence in sentences:
   # strip the leading/trailing whitespace and ensure the sentence isn't empty
   cleaned_sentence = sentence.strip()
   if cleaned_sentence: # Avoid printing empty sentences
      print(f"{cleaned_sentence}")



