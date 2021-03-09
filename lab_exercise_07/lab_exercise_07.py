# START LAB EXERCISE 07
print('Lab Exercise 07 \n')

# SETUP
houseplants = [
    {"Name": "Areca Palm", "Max height": "8 feet", "Water": "Low", "Sunlight": "Part shade"},
    {"Name": "Parlor Palm", "Max height": "6 feet",  "Water": "Medium" , "Sunlight": "Part shade"},
    {"Name": "Aloe Vera", "Max height": "2 feet",  "Water": "Low", "Light": "Full sun"},
    {"Name": "Snake Plant", "Max height": "2 feet",  "Water": "Medium" , "Light": "Part shade"},
    {"Name": "Lucky Bamboo", "Max height": "3 feet",  "Water": "Medium" , "Light": "Part shade"}
]

new_houseplants = [
    ["Golden Pothos", "8 feet", "Medium", "Part shade"],
    ["Weeping Fig", "10 feet", "Medium", "Full sun"],
    ["Prayer Plant", "2 feet", "High", "Part shade"]
]
# END SETUP

# PROBLEM 1 (4 Points)
def avg_height(plants):
    """
    This function loops through a list of dictionaries, changes value assigned to <"Max height">
    from a string to an integer, and calculates average <"Max height"> value among all plants in the
    plants list.

    Parameters:
        plants (list): list of dictionaries representing plants and their characteristics.

    Return:
        int: average value among all values assigned to the key <"Max height">.
    """
    pass


# PROBLEM 2 (4 Points)
def add_plants(new_plants, plants):
    """
    This function takes in a nested list and list of dictionaries, alters the nested list into a
    key:value pair format, and appends the new key:value pairs to the list of dictionaries

    Parameters:
        new_plants (list): nested list with values that need to be transformed into key:value pairs that match
        that of the <houseplants> list.

        plants (list): list of dictionaries representing plants and their characteristics.

    Returns:
        list: list of dictionaries representing plants and their characteristics with 
        newly added plants.
    """
    pass


# PROBLEM 3 (4 Points)
def large_plants(plants):
    """
    This function compares the values assigned to the key <"Max height"> to the average among all
    the values assigned to <"Max height"> using the <avg_height()> function.

    Parameters:
        plants (list): list of dictionaries representing plants and their characteristics.

    Returns:
        list: list of dictionaries that have a value assigned to <"Max height"> larger than the average
        of all values assigned to <"Max height">.
    """
    pass


# PROBLEM 4 (4 Points)
def soil_level(plants):
    """
    This function adds the key <"Soil">. The key is based on the values assigned to the key <"Water">.
    If the value to <"Water"> is <"Low">, then value of <"Soil"> is <"Dry"> if <"Water"> is <"Medium">,
    then <"Soil"> is <"Slightly dry">, and if <"Water"> is <"High">, then <"Soil"> is <"Never dry">.

    Parameters:
        plants (list): list of dictionaries representing plants and their characteristics.

    Returns:
        list: list of dictionaries representing plants and their characteristics with
        the key <"Soil"> added and its assigned values.
    """
    pass


# PROBLEM 5 (4 Points)
def main():
    """Program entry point. Handles the program workflow.

    Parameters:
        None

    Returns:
        None
    """
    new_houseplants_list = None
    print(f'New houseplants list: {new_houseplants_list}')

    large_houseplants = None
    print(f'Large houseplants: {large_houseplants}')

    final_houseplants = None
    print(f'Final houseplants list: {final_houseplants}')


if __name__ == '__main__':

    main()

# END LAB EXERCISE