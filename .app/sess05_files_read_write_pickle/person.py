# Python file/module to define a Person class

class Person:
   def __init__(self, name,age,gender):
      """
      Constructor for the Person class.

      :param name(str): the person's name.
      :param age(int): the person's age.
      :param gender(str): the person's gender.
      """
      self.name = name
      self.age = age
      self.gender = gender