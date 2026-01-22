"""
Python Lists
A Python list is a built-in data type that represents an ordered collection of items/elements that are
homogeneous in nature.
Lists allow duplicates and are mutable (i.e. their elements can be modified, added or removed).
Lists are created using the [] or the list() constructor.
A sample list and some of its operations are given below.
"""

# Create a list of fruits
fruits = ["apple", "banana", "cherry "]

# Display the fruits in fruit list
print(f"The original/initial fruits in the fruit list are: {fruits}")

# Display the number of items/elements in the fruit list
print(f"The number of fruits in the fruit list is: {len(fruits)}")

# Add a fruit to the end of the fruit list
fruits.append("orange")
print(f"After adding 'orange' to the fruit list we get: {fruits}")

# Add the contents of another list of fruits to our fruit list
fruits.extend(["pineapple","grapes","avocado","mango","apple"])
print(f"The combined list of fruits is:\n{fruits}")

# Insert a fruit (item/element) at a given index
fruits.insert(1,'pear')
print(f"After inserting 'pear' to the fruit list we get:\n{fruits}")

# Remove a fruit (item/element) at a given index
removed_fruit = fruits.pop(3)
print(f"After removing {removed_fruit} from the fruit list we get:\n{fruits}")

# Remove a fruit (item/element) from the list using its name
fruits.remove("banana")
print(f"After removing'banana' from the fruit list we get:\n{fruits}")

# Get and display the index of a given item/element in list
print(f"The first occurence of 'mango' is at index: {fruits.index('mango')}")

# Get and display the occurence(s) of a given item/element in the list
print(f"'apple' occurs {fruits.count('apple')} time(s) in the fruit list.")

# Sort and display the fruits in ascending/alphabetical/lexicographical order
fruits.sort()
print(f"After sorting the fruit list in ascending/lexicographical order we get:\n{fruits}")

# Sort and display the fruits in descending/ reverse lexicographical order
fruits.reverse()
print(f"After sorting the fruit list in descending or reverse lexicographical order we get:\n{fruits}")

# Get and display the minimum and maximum item/element in the fruit list i.e.
# the least and highest fruits letterwise
print(f"The least fruit letter-wise is: {min(fruits)}"
      f"\nThe highest fruit letter-wise is: {max(fruits)}")

# Get and display a copy of the fruit list
copy_of_fruits = fruits.copy()
print(f"The copied list of fruits is:\n{copy_of_fruits}")

# Remove all the fruits from the fruit list and display the empty list
fruits.clear()
print(f"After removing all fruits from list we get:\n{fruits}")