# Python script to demonstrate a custom iterator

class PlusCounter:
   """
   A simple iterator class that counts from a starting number to an end number,
   incrementing by a specified step.

   Attributes:
      current (int): The current value in the iteration.
      end (int): The maximum value (inclusive) the counter should reach.
      step (int): The number by which the counter should be incremented on each iteration.
   """

   def __init__(self, start, end, step=1):
      """
      Initialises the PlusCounter object/instance.

      Args:
      :param start (int): The starting value for of the counter.
      :param end (int): The maximum value (inclusive) the counter should reach.
      :param step (int): The number by which the counter should be incremented on each iteration.
      """
      self.current = start
      self.end = end
      self.step = step

   def __iter__(self):
      """
      Returns a new iterator object.

      Returns:
         PlusCounter: The new iterator object.
      """
      return self

   def __next__(self):
      """
      Returns the next value in the iteration/sequence.

      Raises:
         StopIteration: When the current value exceeds the end/maximum value.

      Returns:
         int: The next value in the iteration/sequence.
      """
      if self.current > self.end:
         raise StopIteration
      else:
         self.current += self.step
         return self.current - 1

# Create/instantiate a PlusCounter object
my_counter1 = PlusCounter(1,10)

# Iterate over the counter object
for num in my_counter1:
   print(num)

print('\n')

# Create another PlusCounter object to give the multiples of 5 from 1 - 75
my_counter2 = PlusCounter(1,75,5)

# Iterate over the counter2 object
for num in my_counter2:
   print(num)
