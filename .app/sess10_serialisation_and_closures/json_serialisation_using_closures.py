# Python script that uses closures to serialise and deserialise a Student object
# to and from a JSON file

# Import the required modules
import json
from datetime import date, datetime
import os

# Define a Student class
class Student:

   # constructor
   def __init__(self, reg_no, name, birthdate,gender):
      self.reg_no = reg_no
      self.name = name
      self.birthdate = birthdate
      self.gender = gender

   # Instance method to convert the student object into a dictionary
   def to_dict(self):
      return {
         'reg_no': self.reg_no,
         'name': self.name,
         'birthdate': self.birthdate.isoformat(),
         'gender': self.gender
      }

   #  Static method to deserialise a dictionary back to a Student object
   @staticmethod
   def from_dict(data):
      return(Student(
         reg_no = data['reg_no'],
         name = data['name'],
         birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date(),
         gender = data['gender']
      ))

# Closures
def student_json_handler(file_path):

   def serialise(student):

      with open(file_path, 'w') as f:
         json.dump(student.to_dict(), f)
      print(f"Student details serialised to JSON successfully in the file:\n{file_path}.")

   def deserialise():

      with open(file_path, 'r') as f:
         data = json.load(f)
         student = Student.from_dict(data)
         print(f"Deserialised student details from the file:\n{file_path}.")
         return student

   return serialise, deserialise

# Run the application
if __name__ == '__main__':
   # Example to create a student object, save then load it using the above closures
   student = Student("DS2509_S8","Abigail Winfred",
                     date(2016,3,25), "Female")
   file_path = os.path.abspath(os.path.join(os.getcwd(),'..','files','students.json'))
   os.makedirs(os.path.dirname(file_path), exist_ok=True) # Ensure the above directory is created to avoid errors
   serialise, deserialise = student_json_handler(file_path)
   serialise(student) # save the student details to the json file
   loaded_student = deserialise() # read in the student details from the json file

   # Display the loaded student details
   print(f"Loaded student details :\n{loaded_student.name}, {loaded_student.birthdate}, {loaded_student.gender}")