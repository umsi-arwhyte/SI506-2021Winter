# SI 506: Lab Exercise 09

## This Week's Lab

This week's lab focuses on creating classes, instantiating classes, class variables, and the initialization of functions and other helper functions.

##  1.0 Problem 01
In this problem, you will:
1. Create a constructor for the `Battery` class
2. Initialize variables

Instance Variable:

* `battery_size` (int): Electric vehicle battery size

The constructor will take the following argument:

* `battery_size`

and assign it to an instance variable of the same name. Additionally the constructor will create the class instance variable called `battery_level` that will be set to the integer 0.
### 1.1 Problem 01
In this problem you will:
1. Create a helper method
2. Use a positional argument to update the class instance

Implement the `get_connector()` method of the `Battery` class by replacing the `pass` statement with the appropriate code block. Read the method Docstring for additional implementation details.
## 2.0 Problem 02 (3 Points)

In this problem, you will:
1. Create a constructor for the `ElectricVehicle` class
2. Initialize variables

Instance Variables:

* `brand` (string): Brand of the ElectricVehicle for the instance.
* `model` (string): Model of the ElectricVehicle for the instance.
* `battery` (instance): Battery instance.
* `passengers` (integer): Number of passengers in the Electric Vehicle for the instance.

The constructor will take the following arguments:

* `self`
* `brand`
* `model`
* `battery`
* `passengers`

and assign each to an instance variable of the same name. Additionally the constructor will create two more instance variables. The first variable called `features` will have an empty list as its variable. We'll change that later when calling the `update_features()` method. The second variable will be called `seat_capacity` and have the number 5 assigned to it as the max number of occupants in the vehicle.

Replace the `pass` statements with the appropriate code blocks. Read the class and method Docstrings for additional implementation details.

## 3.0 Problem 03 (3 Points)

In this problem you will:
1. Create a method to update the class instance

Implement the `increment_passengers()` method of the `ElectricVehicle` class by replacing the `pass` statement with the appropriate code block. Read the method Docstring for additional implementation details.

## 4.0 Problem 04 (3 Points)

In this problem you will:
1. Create a helper method
2. Use a positional argument to update class instance

Implement the `update_features()` method of the `ElectricVehicle` class by replacing the `pass` statement with the appropriate code block. Read the method Docstring for additional implementation details.

## 5.0 Problem 05 ( Points)

In this problem you will:
1. Create a method to update the class instance

Implement the `charge()` method of the `ElectricVehicle` class by replacing the `pass` statement with the appropriate code block. Read the method Docstring for additional implementation details.
## 6.0 Problem 06 (3 Points)

In this problem you will:
1. Override the `__str__()` method to represent the `ElectricVehicle` class

Implement the `__str__()` method of the `ElectricVehicle` class by replacing the `pass` statement with the appropriate code block. Read the method Docstring for additional implementation details.

## 7.0 Problem 07 (3 Points)

In this problem, you will:
1. Instantiate an object
2. Update the instance's variables.
### 7.1: Create `tesla`

1. Instantiate a `ElectricVehicle` object with "Tesla" as the `brand`, "Model 3 Performance AWD" as the `model`, 100 as the `battery_size`, and 4 as the `passengers`. Assign this object to the variable `tesla`.
2. Call the `increment_passengers()` method on `tesla` two times. This should print the string "The vehicle has reached full capacity." you created in Problem 3.

:bulb: You can use a for loop and `range()` to help repeat functions/methods several times.
3. Call the `update_features()` twice to add the features "cruise control" and "heated seats".
4. Call the `get_connector` method on `tesla`. Print the return value to view the connector type.
5. Print `tesla` to display the vehicle that is driving.

### 7.2: Create `nissan`

1. Instantiate an `ElectricVehicle` object with "Nissan" as the `brand`, "Leaf" as the `model`, 40 as the `battery_size`, and 2 as the `passengers`. Assign the object to `nissan`.
2. Call the `charge()` method on `nissan`. This should print the string "The vehicle is now fully charged." you created in Problem 5.
3. Print the `battery_level` to ensure it is at 40 and not 0.
4. Call the `get_connector` method on `nissan`. Print the return value to view the connector type.
5. Print `nissan` to display the vehicle that is driving.
