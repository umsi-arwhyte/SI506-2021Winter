# START LAB EXERCISE 08
print('Lab Exercise 08 \n')

import os

# PROBLEM 2
def get_links_by_categories(links, categories):
    """
    This function returns a filtered list of library database category permalinks
    based on one or more passed in categories. Each permalink in the passed in
    list is represented as a string that also includes the permalink's assigned
    category and academic discipline, each separated by a comma per the
    following format:

    '< category >, < discipline >, < permalink URL >'

    If a case-insensitive category match is obtained the function converts the
    permalink string representation to a list per the following format:

    ['< category >', '< discipline >', '< permalink URL >']

    and stores it locally in a list before returning the local list of nested
    permalink lists to the caller after checking all passed in links elements.

    Parameters:
        links (list): a list of strings that represent library database permalinks.
        categories (list): list of categories used as filters

    Returns:
        list: A filtered list of permalink lists
    """

    pass # TODO Implement

# PROBLEM 1
def read_file(filepath):
    """Reads text file and returns each line as a list element.

    Parameters:
        filepath (str): path to file

    Returns
        list: list of lines in file
    """

    pass # TODO Implement

# PROBLEM 3
def write_file(filepath, data):
    """Write content to a target file encoded as UTF-8. Each element in the passed
    in sequence is written to a new line.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of strings comprising the content to be written to the target file

    Returns:
        None
    """

    pass # TODO Implement


def main():
    """
    Entry point for the program. This function will process the library data.

    Parameters:
        None

    Returns:
        None
    """

    filepath = 'library_databases.txt' # Gradescope

    # DEBUGGER USE ONLY (COMMENT OUT BEFORE SUBMITTING TO GRADESCOPE)
    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # filepath = os.path.join(abs_path, 'library_databases.txt')

    # PROBLEM 01
    links = None
    # print(f"\n1.0 {links}")

    # PROBLEM 02
    filtered_links = None
    # print(f"\n2.0 {filtered_links}")

    # PROBLEM 03

    # TODO call write_file() twice

if __name__ == '__main__':
    main()
