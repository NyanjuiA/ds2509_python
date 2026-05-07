# Python scripto demonstrate OOP concepts of Data Hiding, Overloading (simulation), and overriding

# Define an animal class
class Animal:
   def __init__(self, name,age):
      self._name = name # Protected by convention
      self.__age = age # Private (name mangled to _Animal__age)

   def get_private_age(self):
      return self.__age # Access the private instance variable __age via a getter

   def speak(self):
      return f"{self._name} makes a sound"

   def make_sound(self, *args): # Simulate overloading with *args(positional) arguments
      base_sound = self.speak()
      if not args:
         return base_sound
      elif len(args) == 1 and isinstance(args[0], (int, float)):
         volume = args[0]
         return f"{base_sound} at volume {volume}"
      else:
         extras = ', '.join(str(args) for args in args)
         return f"{base_sound} with extras: {extras}"

class Dog(Animal):
   def __init__(self, name, age):
      super().__init__(name, age)

   def speak(self): # Override the Animal's  (parent class) speak method
      return f"{self._name} barks 'WOOF' loudly!"

# Intantiate a dog object and call the various methods
dog = Dog("Jimmy",5)
print(dog.speak()) # Overriding the Animal'sl speak() method
print(dog.make_sound()) # Overloading simulation: no arguments passed
print(dog.make_sound(8)) # Overloading simulation: volume argument of 8 passed
print(dog.make_sound(12, "with toy","excited")) # Overloading simulation: volume and extras argument passed
print(f"Jimmy's age: {dog.get_private_age()} years.") # Data hiding: age accessed via getter
# print(dog.__age) # Error: Not directly accessible (but mangled: dog._Animal__age works)