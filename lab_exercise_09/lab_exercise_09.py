# LAB EXERCISE 09
print('Lab Exercise 09')

# PROBLEM 1 (5 Points)
class Battery():
    """
    This Battery class helps instantiate the Battery objects later used
    in the lab exercise. This contains the init function a helper model.
    """

    def __init__(self, battery_size):
        """
        This function initializes the class with following variables:
        1. < battery_size > : updated using the passed positional argument < battery_size >
        2. < battery_level > : initialized as an the integer 0

        Parameters:
            battery_size (integer): Battery size of the ElectricCar for the instance.

        Returns:
            None
        """

        pass


# PROBLEM 1.1
    def get_connector(self):
        """
        This function returns the connector type depending on the battery size. If the battery size
        is greater than or equal to 75 than the connector type is Tesla and the string "Tesla" will
        be returned. If the battery size is less than 75 then the connector type is J1772 and the
        string "J1772" will be returned.

        Parameters:
            None

        Returns:
            string: connecter type "Tesla" or "J1772" dependending on battery_size.
        """

        pass


# PROBLEM 2 (3 Points)
class ElectricVehicle:
    """
    This ElectricVehicle class helps instantiate the ElectricVehicle objects later in the lab exercise.
    This contains the init function and helper models.
    """

    def __init__(self, brand, model, battery, passengers):
        """
        This function initializes the class with the following variables:
        1. < brand > : updated using the passed positional argument < brand >
        2. < model > : updated using the passed positional argument < model >
        3. < battery > : initialized using the Battery class
        4. < passengers > : updated using the passed positional argument < passengers>
        5. < features > : initialized as an empty list
        6. < seat_capacity > : initialized as the set integer 5

        Parameters:
            brand (string): Brand of the ElectricVehicle for the instance.
            model (string): Brand of the ElectricVehicle for the instance.
            passengers (integer): Number of passengers in the ElectricVehicle for the instance.

        Returns:
            None
        """

        pass


    # PROBLEM 3 (3 Points)
    def increment_passengers(self):
        """
        This function updates the < passenger > class variable's value by 1
        as long as the < passenger > value is less than the < seat_capacity > value
        of 5. If the vehicle has reached full capacity meaning the < passenger > value
        is equal to the < seat_capacity > then no more passengers are added and
        the following statement is printed: "The vehicle has reached full capacity."

        Parameters:
            None

        Returns:
            None
        """

        pass


    # PROBLEM 4 (1.5 Points)
    def update_features(self, feature):
        """
        This function updates the < features > list with the value provided from the
        < feature > argument. Append < feature > to < features >.

        Parameters:
            feature (string): New feature to add to the instance.

        Returns:
            None
        """

        pass


    # PROBLEM 5 (1.5 Points)
    def charge(self):
        """
        This function updates the < battery_level > value to the < battery_size > value
        and prints the following statement: "The vehicle is now fully charged."

        Parameters:
            None

        Returns:
            None
        """

        pass


    # PROBLEM 6 (3 Points)
    def __str__(self):
        """
        This function returns the string representation of the object.

        Parameters:
            None

        Returns:
            string: the string representation of the object. This should
            return the following string:
            "The < brand > < model > is currently driving."
        """

        pass


# PROBLEM 7 (3 Points)

# Create Tesla
tesla = None

# Create Nissan
nissan = None

# END LAB EXERCISE
