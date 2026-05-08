# Python script to demonstrate MySQL database CRUD operations
# NB: install the mysql python connector module => pip install mysql-connector-python

# -------------------------------------------------------------------------------------------
# Import the required modules
# -------------------------------------------------------------------------------------------
import mysql.connector
from db_conn import db_config
from student import Student

# -------------------------------------------------------------------------------------------
# Function to connect to the MySQL database
# -------------------------------------------------------------------------------------------
def connect_to_database():
   """
   Establish a connection to the MySQL database

   This function attempts to connect to the MySQL database using the configuration
   details/parameters imported from db_conn. When successful, it returns a connection
   object; otherwise, it returns None.

   Returns
      connection: A MySQL connection object if successful, None otherwise.
   """
   try:
      connection = mysql.connector.connect(**db_config)
      if connection.is_connected():
         print("Connected to MySQL ds2509 database!")
         return connection
   except mysql.connector.Error as err:
      print(f"Error: Unable to connect to MySQL \n{err}")
      return None

# -------------------------------------------------------------------------------------------
# Function to close the database connection
# -------------------------------------------------------------------------------------------
def close_connection(connection):
   """
   Close the active MySQL connection.

   This function safely closes the provided database connection if it exists.

   Parameters
      :param connection:  The MySQL connection object to be closed.
   """
   if connection:
      connection.close()
      print("MySQL connection closed")

# -------------------------------------------------------------------------------------------
# Function to get/fetch student details from the ds2505 database
# -------------------------------------------------------------------------------------------
def read_students(connection):
   """
   Retrieve and display all student records from the student table.

   This function executes a SELECT query to fetch all the student records from
   the database, creates 'Student' objects from each record, and prints them.

   Args:
      :param connection: An active MySQL database connection
   :return:
   """
   try:
      cursor = connection.cursor()
      select_query = "SELECT * FROM Student"
      cursor.execute(select_query)
      students = cursor.fetchall()
      for student in students:
         student = Student(*student)
         print(student)
   except mysql.connector.Error as err:
      print(f"Error: Unable to get student details from MySQL \n{err}")

# -------------------------------------------------------------------------------------------
# Function to add/insert a student record into the Student table in the ds2505 database
# -------------------------------------------------------------------------------------------
def insert_student(connection,student:Student):
   """
   Insert a new student record into the Student table.

   This function takes a 'Student' object and inserts its data as a new record in the ds2509 database.The
   changes are committed to the database to make them permanent.

   Args:
      :param connection: An active MySQL database connection.
      :param student: A 'Student' object containing the student details to be inserted into the student table.
   """
   try:
      cursor = connection.cursor()
      insert_query = """
      INSERT INTO Student(Student_No, Name, Birthdate,Gender)
      value(%s, %s, %s, %s)
      """
      student_data = (student.student_no, student.name, student.birthdate, student.gender)
      cursor.execute(insert_query, student_data)
      connection.commit() # Save/store/commit the changes to the ds2509 database
      print(f"Student {student.student_no} inserted successfully")
   except mysql.connector.Error as err:
      print(f"Error: Unable to insert student details into MySQL,\n{err}")
   finally:
      cursor.close() # Close the cursor
      # close_connection(connection) # close the database connection

# -------------------------------------------------------------------------------------------
# Function to modify/update a student record into the Student table in the ds2505 database
# -------------------------------------------------------------------------------------------
def update_student(connection,student:Student):
   """
   Update an existing student record in the Student table.

   This function updates a student's record based on their student number.
   When the record is found and updated, a success message is displayed.

   Args:
      :param connection:  An active MySQL database connection.
      :param student: A 'Student' object containing the update student details.
   """
   try:
      cursor = connection.cursor()
      update_query = """
      UPDATE Student
      set Name = %s, Birthdate = %s, Gender = %s
      WHERE Student_No = %s
      """
      student_data = (student.name, student.birthdate, student.gender, student.student_no)
      cursor.execute(update_query, student_data)
      connection.commit()
      if cursor.rowcount > 0:
         print(f"Student {student.name}'s record updated successfully!")
      else:
         print(f"Error: Student {student.name}'s record could not be updated or found!")
   except mysql.connector.Error as err:
      print(f"Error: Unable to update student details into MySQL,\n{err}")
   finally:
      cursor.close()

# -------------------------------------------------------------------------------------------
# Function to delete a student record from the Student table in the ds2505 database
# -------------------------------------------------------------------------------------------
def delete_student(connection,student_no:str):
   """
   Delete an existing student record in the Student table.

   This function removes a student record identified by their student number.
   It confirms where the deletion was successful or if the record was not found.

   Args:
      :param connection: An active MySQL database connection.
      :param student_no (str): The student number of the record to be deleted.
   """
   try:
      cursor = connection.cursor()
      delete_query = "DELETE from Student where Student_No = %s"
      cursor.execute(delete_query, (student_no,))
      connection.commit()
      if cursor.rowcount > 0:
         print(f"Student {student_no}'s record deleted successfully!")
      else:
         print(f"Error: No record with the given student number was found!\n"
               f"Kindly check the student number and try again.")
   except mysql.connector.Error as err:
      print(f"Error: Unable to delete student details from the database,\n{err}")
   finally:
      cursor.close()

# -------------------------------------------------------------------------------------------
# Run the script to perform the CRUD operations against the ds2505 database
# -------------------------------------------------------------------------------------------
if __name__ == "__main__":
   connection = connect_to_database()

   if connection:
      # Create some Student objects
      new_student1 = Student('EICN-DS2509-S0007', 'Faith Wanjiru',
                         '1998-10-17','F')
      dummy_student = Student('EICN-DS2509-S0006', 'Some Dummy Student',
                            '1999-11-15', 'F') # Will be deleted later

      # Get all the students from the database
      read_students(connection)

      # Add/insert the above students' details to the Student table in the ds2509 database
      # insert_student(connection, new_student1)
      # insert_student(connection, dummy_student)

      # Update the dummy student's details
      # dummy_student = Student('EICN-DS2509-S0006', 'Update Dummy Student',
      #                         '2001-11-15', 'F')
      # update_student(connection, dummy_student)

      # Delete the dummy student's record
      # delete_student(connection, 'EICN-DS2509-S0006')

      read_students(connection)

   close_connection(connection)



