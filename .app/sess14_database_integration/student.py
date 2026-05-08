# Python script to define a Student class that maps to the Student table in the MySQL database

class Student:

   def __init__(self, student_no, name, birthdate, gender):
      """
      Represents a student in a learning institution.

      Attributes:
         student_no (str): The student's unique identifier.
         name (str): The student's name.
         birthdate (date): The student's date of birth.
         gender (str): The student's gender. ('M' or 'F').'
      """
      self.student_no = student_no
      self.name = name
      self.birthdate = birthdate
      self.gender = self._validate_gender(gender)

   def _validate_gender(self, gender):
      """
      Validate the gender parameter to be either 'M' or 'F'.

      Args:
         gender (str): The gender value to be validated.

      Raises:
         ValueError: If the gender value is not 'M' or 'F'.'

      Returns:
         str: The validated gender value.
      """
      if gender not in ['M','F']:
         raise ValueError("Invalid gender.\nGender must be 'M' or 'F'.")
      return gender

   def __str__(self):
      """
         Returns a string representation of the student.

         Returns:
            str: A human-readable string showing the student's details.
      """
      gender_str = "Male" if self.gender == 'M' else "Female"
      return (f"Student: {self.name} (Student No: {self.student_no}, "
              f"Date of Birth: {self.birthdate}, Gender: {gender_str}) )")