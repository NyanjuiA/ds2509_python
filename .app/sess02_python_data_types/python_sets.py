"""
Python Sets
A set is a built in data type that represents an unordered collection of elements of the same
or different types.
Sets DON'T allow duplicates but are mutable and are useful for tasks that involve checking membership,
removing duplicates, and performing mathematical set operations like
intersection, union, difference, and symmetric difference.
Sets are created using the curly braces/brackets {} or the set() constructor.
Some set operations are given below:
"""

# Create a set of fruits
fruits = {'apple', 'banana', 'cherry', 'durian','elephant apple'}

# Display the contents of the fruit set
print(f"The contents of the 'fruits' set are:\n{fruits}")

# Display the number of fruits in the set
print(f"The number of fruits in the 'fruits' set is: {len(fruits)}")

# Add 'orange' to the set of fruits
fruits.add('orange')
print(f"After adding 'orange' to the set of fruits we get:\n{fruits}")

# Remove 'banana' from the set of fruits
fruits.remove('banana')
print(f"After removing 'banana' from the set we get:\n{fruits}")

# Discard a fruit from the set and display the remaining fruits
fruits.discard('cherry')
print(f'After discarding "cherry" from the "fruits" set we get:\n{fruits}')

# Remove the last fruit from the fruits set
popped_fruit = fruits.pop()
print(f"After popping '{popped_fruit}' from the 'fruits' set we get:\n{fruits}")

# Declare another set of fruits
more_fruits = {'pear','avocado','mango','pineapple'}

# Create a combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined set of fruits is:\n{combined_fruits}")

# Copy the remaining set of original fruits and display them
copy_of_fruits = fruits.copy()
print(f"After copying the remaining set of fruits to a new set we get:\n{copy_of_fruits}")

# Get and display the common fruits in the 'fruits' and 'more_fruits' sets
common_fruits = fruits.intersection(more_fruits)
print(f"The common set of fruits in 'fruits' and 'more_fruits' sets are:\n{common_fruits}")

# Get and display the fruits that are in the 'fruits' set but not in the 'more_fruits' set
difference_fruits = fruits.difference(more_fruits)

# Get and display the fruits that are either in 'fruits' set or 'more_fruits' set but not both
symmetric_difference_fruits = fruits.symmetric_difference(more_fruits)
print(f"The fruits that are either in 'fruits' set or 'more_fruits' set but not in both"
      f" are:\n{symmetric_difference_fruits}")

# Check whether 'fruits' set is a subset of 'more_fruits' set
is_subset_of_more_fruits = fruits.issubset(more_fruits)
print(f"'fruits' set is a subset of 'more_fruit': {is_subset_of_more_fruits}")

# Check whether 'fruits' set is a superset of 'more_fruits' set
is_superset_of_more_fruits = fruits.issuperset(more_fruits)
print(f"'fruits' set is a superset of 'more_fruit': {is_superset_of_more_fruits}")

# Check and display whether 'fruits' set and 'more_fruits' sets have no common fruits/elements
is_disjoint_fruits = fruits.isdisjoint(more_fruits)
print(f"'fruit' set and 'more_fruit'  have no common fruits/elements: {is_disjoint_fruits}")

# Create another fruit set and use it to update the set of 'fruits'. CAUTION...overwrites set elements
other_fruits = {'watermelon','strawberry','blueberry'}
fruits.update(other_fruits)
print(f"After updating the 'fruit' set we get:\n{fruits}")

# Clear and display the 'fruits' set
fruits.clear()
print(f'After clearing the "fruits" set we get:\n{fruits}')






