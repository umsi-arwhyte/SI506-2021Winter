# SI 506: Lab Exercise 10

#### This Week's Lab

The following lab exercise will allow you to work more with SWAPI to get you
comfortable with using requests module. This week we are retrieving information on the
Star Wars character, Darth Vader, from SWAPI.

Darth Vader is the alter ego of Anakin Skywalker, which means the Dark Lord of the Sith. His alter ego was created when Skywalker turned to the dark side of the Force, pledging his allegiance to the Sith Lord Darth Sidious at the end of the Republic Era.

Source: https://starwars.fandom.com/

## PROBLEM 01 (2.5 Points)

In this problem you will implement `get_resource()` by:
1. Create a GET request
2. Decode the JSON response and work with the resulting dictionary's key-value pairs.

Send a GET request to SWAPI using `{'search': name}` as params value
and store it as a dictionary.

Access the element(s) in the `results` list (if any) and assign the value to the variable named `result`.

:bulb: response['results'][0]
:bulb: convert your response to JSON object using `response.json()`

## PROBLEM 02 (10 Points)

In this problem you will create a constructor (i.e., the __init__ method) for the `Person` class and initialize it and initialize it's variables.

Instance Variables:
* `name` (string): Name of the Star Wars character.
* `hair_color` (string): Star Wars character's hair color.
* `eye_color` (string): Star Wars character's eye color.
* `species` (string): Name of the species of the Star Wars character.

Implement `jsonable()`. This method returns a JSON-friendly representation of the object.
Use a dictionary literal rather than a built-in dict() to avoid built-in lookup costs.

A dictionary literal is created by surrounding key/value pairs with curly braces (`{}`) like so:

```python
    dict_literal = {
        'one': 1,
        'two': 2,
    }
```

Implement `__str__` method. This method will return only the name of the character.

## PROBLEM 03 (2.5 Points)

In this problem you will implement `write_json()`. This function takes in a filepath and data to write to the filepath.

❗ For the `open()` parameters, use `encoding= 'utf-8'` and for the
`json.dump()` parameters, use `ensure_ascii= False`, `indent=2`.

## PROBLEM 04 (10 Points)

In this problem you will implement `main()`:

1. Call `get_resource()` with the correct parameters. Since we are retrieving information on Darth Vader, you will pass to the function a dictionary comprising a single key-value pair: `{'search: 'Darth Vader'}`. Use the "results" key and index the dictionary representation of the decoded JSON to access the resource(s) matched by the search query return. Save the results to `vader_data`.
2. The species key from the response results contains a url. You will need to retrieve Darth Vader's species by making another request to the url within the species key. Assign the name of Darth Vader's species to the variable `vader_species` then update `vader_data` by adding Darth Vader's species name as a key/value pair.
3. Create an instance of `Person` for Darth Vader using the data you have stored in `vader_data` and `vader_species`.
4. Write out the information produced from the instance of `Person` you have created for Darth Vader as a dictionary to a new file `DarthVader.json`.

:hint: Use the `jsonable()` method to transform the class instance into a dictionary.
