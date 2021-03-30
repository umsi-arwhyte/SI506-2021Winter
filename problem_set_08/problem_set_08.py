import csv
# Problem 01
def read_txt(filepath):
    """
    This function takes a filepath as an argument and returns a list of strings, each being a line from the txt file.
    Before adding a line to the list, this function should first remove any newline (\n) characters from that string

    Parameters:
        filepath (str): A filepath for a txt file

    Returns
        (list): A list of strings, each being a line in from the txt file (with the newlines removed)
    """
    pass

# Problem 02
def write_txt(filepath, data):
    """
    This function takes a filepath and a list of lists as arguments and outputs each actress along with the movie they
    starred in to a txt file. When outputting to the txt file specified in the filepath, the each line should have the following
    format:

    < actress > - < film >

    Parameters:
        filepath (str): A filepath for a txt file to be written to
        data (list): A list of lists, each representing an actress and the movie she starred in

    Returns:
        None
    """
    pass

# Problem 03
def read_csv(filepath):
    """
    This function takes a filepath for a csv as an argument and returns a list of dictionaries, each
    representing a film.

    The newly created dictionaries will have the following format:
    {
        'Category': < category >,
        'Title': < film title >,
        'Director(s)': < film director(s)
    }

    Parameters:
        filepath (str): A filepath of a csv file to be read from

    Returns:
        (list): A list of dictionaries, each representing a film
    """
    pass

# Problem 04
def sort_films(film_list):
    """
    This function takes a list of film dictionaries as an argument and sorts each film by category.
    Create a dictionary where the keys are the names of the film categories and the values are initially empty lists,
    then loop through the list of films and add each film to the list with the approriate category.
    The final dictionary should have the following format:
    {
        'Animated Feature Film': < list of Animated Feature Film  nominees >,
        'Best Picture': < list of Best Picture nominees >,
        'Documentary (Feature)': < list of Documentary (Feature) nominees >,
        'International Feature Film': < list of International Feature Film nominees >,
        'Short Film (Live Action)': < list of Short Film (Live Action) nominees >
    }

    Parameters:
        film_list (list): A list of dictionaries, each representing a film

    Returns:
        (dict): A dictionary with five key:value pairs
    """
    pass

# Problem 05
def write_csv(filepath, data):
    """
    This function takes a csv filepath and a list of dictionaries as arguments and outputs them
    to the specified csv file. 

    Parameters:
        filepath (str): A filepath of a csv file to be written to
        data (list): A list of dictionaries, each representing a film

    Returns:
        None
    """
    pass

def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """
    # Problem 01
    print("Problem 01:\n")
    best_actors = None

    # Problem 02
    print("Problem 02:\n")
    best_actresses = [
        ['Viola Davis', 'Ma Rainey\'s Black Bottom'],
        ['Andra Day', 'The United States vs. Billie Holiday'],
        ['Vanessa Kirby', 'Pieces of a Woman'],
        ['Frances McDormand', 'Nomadland'],
        ['Cary Mulligan', 'Promising Young Woman']
    ]

    # Problem 03
    print("Problem 03:\n")
    films = None

    # Problem 04
    print("Problem 04:\n")
    sorted_films = None

    animated_films = None
    best_films = None
    documentaries = None
    international_films = None
    short_films = None

    # Problem 05
    print("Problem 05:\n")

if __name__ == '__main__':
    main()