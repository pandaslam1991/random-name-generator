# Import the random module to allow random selection
import random

# Define a list of names to choose from
names = ["John", "Bill", "Chris", "Charlie"]

# Check if the list is empty
if len(names) == 0:
    # If the list is empty, print an error message
    print("Error: No names available.")
else:
    # Use random.choice() to select one random name from the list
    random_name = random.choice(names)

    # Output the randomly selected name
    print("Randomly selected name:", random_name)
