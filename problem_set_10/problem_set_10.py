import requests, csv, json

# Problem 01
def get_swapi_resource(resource, params=None, timeout=20):
    """
    This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. <params> is not included in the request if no params is passed to this
    function during the function call. Once a response is received, it is converted to a python dict.
    Parameters:
        resource (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments. The default value is None.
        timeout (int): timeout value in seconds. The default value is 20.
    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    pass # TODO: Replace

# Problem 02
def read_json(filepath):
    """
    This function reads in a JSON file and converts it into a dictionary and returns it.
    Parameters:
        filepath(str): The location and filename of the JSON file
    Returns:
        data(dict): A parsed dictionary of resources.
    """
    pass # TODO: Replace

# Problem 03
def write_json(filepath, data):
    """
    This function dumps the JSON object in the dictionary <data> into a file on
    <filepath>.
    Parameters:
        filepath(str): The location and filename of the file to store the JSON
        data(dict): The dictionary that contains the JSON representation of the objects.
    Returns:
        None
    """
    pass # TODO: Replace

# Problem 05
def convert_to_film(film_dict):
    """
    This function converts a film resource dictionary to a <Film> object. The
    <film_dict> can be a dictionary returned by <get_swapi_resource> or by <read_json>.
    It gets the values necessary to instantiate the <Film> class from the keys in the <film_dict>.
    Parameters:
        film_dict (dict): A dictionary representing a film
    Returns:
        (Film): An instance of the film class with values taken from the <film_dict>
    """
    pass # TODO: Replace

# Problem 07
def convert_to_person(person_dict):
    """
    This function converts a person resource dictionary to a <Person> object. The
    <person_dict> can be a dictionary returned by <get_swapi_resource> or by <read_json>.
    It gets the values necessary to instantiate the <Person> class from the keys in the <person_dict>.
    It also updates the <Person> object's list of films to be <Film> objects instead of urls.
    Parameters:
        person_dict (dict): A dictionary representing a person
    Returns:
        (Person): An instance of the person class with values taken from the <person_dict>
    """
    pass # TODO: Replace

#Problem 04
class Film():
    """"
    Representation of a Film.
    Attributes:
        title(str): title of the film
        episode_id(str): the episode number of the film
        year(int): The year the film was released
        url(str): the url of the film
    """
    def __init__(self, title, episode_id, year, url):
        """
        The constructor of the <Film> class. This method takes in the given parameters
        and assigns them to the attributes (instance variables) of the class.
        Parameters:
            title(str): title of the film
            episode_id(str): the episode number of the film
            year(int): The year the film was released
            url(str): the url of the film
        Returns:
            None
        """
        pass # TODO: Replace

    def __str__(self):
        """
        This method provides a readbale string representation of the object.
        Parameters:
            None
        Returns:
            An f-string with the syntax: 'Star Wars: Episode <episode_id> - <title> was released in <year>.'
        """
        pass # TODO: Replace

    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the <Film> object.
        The key should be the name of instance variable and value should be the corresponding value.
        For example, self.title should be converted in this way:
        {"title": self.title}
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        pass # TODO: Replace

# Problem 06
class Person():
    """
    Representation of a Person
    Attributes:
        name(str): Name of the person
        skin_color(str): Color of skin
        hair_color(str): Color of hair
        eye_color(str): Color of eye
        gender(str): Gender
        films(list): List of films the person appears in
        url(str): URL to the person
    """
    def __init__(self, name, skin_color, hair_color, eye_color, gender, films, url):
        """
        The constructor of the <Person> class. This method takes in the given parameters
        and assigns them to the attributes (instance variables) of the class.
        Parameters:
            name(str): Name of the person
            hair_color(str): Color of hair
            skin_color(str): Color of skin
            eye_color(str): Color of eye
            gender(str): Gender
            films(list): List of films the person appears in
            url(str): URL to the person
        Returns:
            None
        """
        pass # TODO: Replace

    def __str__(self):
        """
        This method provides a readable string representation of the object.
        Parameters:
            None
        Returns:
            An f-string with the syntax: "<name> has <hair_color> hair and <eye_color> eyes."
        """
        pass # TODO: Replace

    def update_films(self):
        """
        This method takes the list of URLS and creates new objects of the <Film> class
        and replaces the <films> instance variable with a list of Film objects. It makes use of the
        <convert_resource_to_film()> method and the <get_swapi_resource_function()>.
        Parameters:
            None
        Retruns:
            None
        """
        pass # TODO: Replace

    def jsonable(self):
        """
        This method returns a JSON-friendly representation of the <Person> object.
        The keys should be the name of instance variables and value should be the corresponding values.
        For example, self.name should be converted in this way:
        {"name": self.name}
        Parameters:
            None
        Returns:
            dict: dictionary of the object's instance variables
        """
        pass # TODO: Replace

def main():
    """
    This function serves as the main point of entry and controls the flow of this Python script

    Parameters:
        None
    Returns
        None
    """
    BASE_URL = 'http://swapi.py4e.com/api'

    #Problem 08
    obi_wan_dict = None # TODO: Assign
    obi_wan = None # TODO: Assign

    #Problem 09
    leia_dict = None # TODO: Assign
    leia = None # TODO: Assign

    #Do not comment out, these are needed for the autograder.
    return obi_wan_dict, obi_wan, leia_dict, leia

if __name__ == '__main__':
    main()
