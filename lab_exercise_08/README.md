# SI 506: Lab Exercise 08

## This week's Lab Exercise

This week's lab exercise focuses on reading from and writing to a file using data sourced from the
U-M Library's collection of database subscriptions. Data for the lab exercise is contained in
`library_databases.txt` which contains a select list of permalinks organized by category and
academic discipline.

## Debugger use

:bulb: if you want to run the debugger without configuring VS Code's `launch.json` file uncomment
_temporarily_ the variables `abs_path` and `filepath` that rely on `os.path` for values:

```python
filepath = 'library_databases.txt' # Gradescope

# Debugger use only
abs_path = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(abs_path, 'library_databases.txt')
```

:exclamation: Before submitting the assignment to Gradescope comment out the two variables that
rely on `os.path` for their values.

## 1.0 Problem 01 (6 Points)

Implement the `read_file()` function.  The function accepts a filepath string and returns each
line in the text file as a list element. Read the Docstring for implementation details.

Return to the `main()` function and call the function by passing the argument `file_path`. Assign
the return value to the variable `links`.

## 2.0 Problem 02 (6 Points)

Implement the `get_links_by_categories` function. The function accepts as arguments a list of
database `links` and a list of one or more `categories` used to filter on the permalink's
category. The function returns a list of lists, with each nested list representing a permalink and
its associated metadata. Read the Docstring for implementation details.

Return to the `main()` function and call the function by passing to it as arguments the `links`
returned from Problem 01 and the list `['health sciences', 'science']`. Assign the return value to
the variable `filtered_links`.

:bulb: Each element in `filtered_links` is itself a list:

```python
[
   ['Health Sciences', 'Family Medicine', 'https://search.lib.umich.edu/databases?filter.academic_discipline=Family+Medicine&sort=title_asc\n'],
   # etc, etc ...
]
```

## 3.0 Problem 03 (8 Points)

Implement the `write_file` function. The function accepts as arguments a filepath string and a
sequence (e.g., `list`). The function _must_ write each list element to its own line in the file.
Read the Docstring for implementation details.

Call the function twice.

1. Call the function and pass to it the filepath string  `'health_sci_links.txt'` and _only_ the
   Health Science category permalinks in `filtered_links`.

2. Call the function again and pass to it the filepath string `'sci_links.txt'` and _only_ the 
   Science category permalinks in `filtered_links`.

:bulb: Call the function `write_file` without assigning the return value (`None`) to a variable.
