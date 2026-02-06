# Python script to write car details (as dictionaries) to a JSON file
# and read them back for display

# Import the required module(s)
from pathlib import Path  # Allows our script to workig with different OSes without '\' or '/'
import json  # Allows our script to write and read JSON format


# Function to write car details
def save_car_data(file_path: Path, car_list: list):
   """
   Saves a list of cars dictionaries to a JSON file.

   :param file_path: Path to the JSON file.
   :param car_list: List of dictionaries containing car data/details.

   """
   try:
      file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory/folder exists
      with file_path.open('w', encoding='utf-8') as file:
         json.dump(car_list, file, indent=4)
      print(f"✅ Car data successfully saved at {file_path}!")
   except Exception as e:
      print(f"❌ Sorry, something went wrong when saving car data!:\n{e}")


# Function to read in the car details
def load_car_data(file_path: Path) -> list:
   """
   Loads car data from a JSON file.

   :param file_path: Path to the JSON file.
   :return: List of dictionaries with car details.
   """
   try:
      with file_path.open('r', encoding='utf-8') as file:
         return json.load(file)
   # Handle errors/exceptions
   except FileNotFoundError as fnf:
      print(f"❌ Sorry, the file was not found!:\n{fnf}")
      return []  # return an empty list
   except json.decoder.JSONDecodeError as jde:
      print(f"❌ Sorry, failed to decode the JSON data.\n{jde}")
      return []
   except Exception as e:
      print(f"❌ Sorry, error loading car data!:\n{e}")
      return []


# Function to display the car details
def display_car_data(car_list: list):
   """
   Displays a list of car dictionaries in a readable format.

   :param car_list: List of dictionaries containing car data.
   """
   if not car_list:
      print("Sorry, no car details were found, nothing to display!")
      return
   print("\n🚘 Car Details")
   print(f"-" * 60)
   for car in car_list:
      print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']},"
            f"Price: Kes. {car['price']}")
   print(f"-" * 60)


# Define car details/data
cars = [
   {"make": "Toyota", "model": "Corolla", "year": 2020, "price": 2000000},
   {"make": "Honda", "model": "Civic", "year": 2021, "price": 2200000},
   {"make": "Ford", "model": "Mustang", "year": 2022, "price": 3500000},
   {"make": "Tesla", "model": "Model 3", "year": 2023, "price": 4000000},
   {"make": "Mazda", "model": "CX-5", "year": 2018, "price": 2400000}
]
# Define the path to save the JSON file: one directory up into the 'files/cars.json'
file_path = Path.cwd().parent / 'files' / 'cars.json'

# Call the above functions to write/save, read and display the car details/data
save_car_data(file_path, cars)
car_details = load_car_data(file_path)
display_car_data(car_details)
