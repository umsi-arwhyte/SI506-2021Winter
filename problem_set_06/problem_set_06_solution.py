subway = {
    'items': ['Spicy Italian', 'Steak & Cheese', 'Meatball Mariana', 'Oven Roasted Chicken'],
    'prices': [5.99, 9.49, 5.29, 8.49],
    'cals': [900, 680, 410, 540]
}

mcdonalds = {
    'items': ['Big Mac', 'Quarter Pounder', 'Chicken McNuggets', 'Filet-O-Fish'],
    'prices': [4.27, 4.06, 4.80, 4.06],
    'cals': [550, 520, 420, 380]
}

burger_king = {
    'items': ['Whopper', 'Crispy Chicken Sandwich', 'Chicken Fries', 'Big Fish Sandwich'],
    'prices': [4.48, 5.34, 7.27, 4.27],
    'cals': [657, 670, 429, 513]
}

taco_bell = {
    'items': ['Cheesy Gordita Crunch', 'Quesarito', 'Crunchwrap Supreme', 'Chalupa Supreme'],
    'prices': [3.59, 3.39, 3.79, 3.19],
    'cals': [500, 650, 530, 350]
}

#Problem 01 (10 points)
def print_menu_items(restaurant):
    """
    Loops through a list of menu items and prints out each item

    Parameters:
        restaurant (dict): A dictionary with three lists items, prices, and cals

    Returns:
        None
    """
    for item in restaurant['items']:
        print(item)

print_menu_items(mcdonalds)

#Problem 02 (20 points)
def most_expensive_menu_item(restaurant):
    """
    Loops through a list of menu items and determines the most expensive item

    Parameters:
        restaurant (dict): A dictionary with three lists items, prices, and cals

    Returns:
        str: A string with the name of the most expensive item
    """
    highest_price = 0
    highest_price_index = None
    for index, price in enumerate(restaurant['prices']):
        if price > highest_price:
            highest_price = price
            highest_price_index = index
    return restaurant['items'][highest_price_index]

most_expensive_taco_bell_item = most_expensive_menu_item(taco_bell)
print(most_expensive_taco_bell_item)

#Problem 03 (40 points)
def create_menu(restaurant):
    """
    Creates a dictionary representation of a new menu item and adds it to the menu.

    Parameters:
        menu (list): A list of dictionaries, each representing a restaurant item
        item (str): A string with the name of a new menu item
        price (float): A flot with the price of the new menu item
        cal (int): An integer with the number of calories for the new menu item

    Returns:
        menu (list): A list of dictionaries, each representing a restaurant item
    """
    menu = []
    for index, item in enumerate(restaurant['items']):
        temp_dict = {
            'Item': item,
            'Price': restaurant['prices'][index],
            'Cal': restaurant['cals'][index]
        }
        menu.append(temp_dict)
    return menu

subway_menu = create_menu(subway)
mcdonalds_menu = create_menu(mcdonalds)
burger_king_menu = create_menu(burger_king)
taco_bell_menu = create_menu(taco_bell)
print(subway_menu)

#Problem 04 (20 points)
def add_menu_item(menu, item, price, cal):
    """
    Loops through a list of menu items and prints out each item with the follwing format:
    < item >: $< price > (< Cal > Cal)

    Parameters:
        menu (list): A list of dictionaries, each representing a restaurant item

    Returns:
        None
    """
    new_dict = {'Item': item, 'Price': price, 'Cal': cal}
    menu.append(new_dict)
    return menu

add_menu_item(taco_bell_menu, 'Nacho Fries', 1.39, 320)

#Problem 05 (15 points)
def print_menu(menu):
    """
    Loops through a list of menu items and prints out each item

    Parameters:
        menu (list): A list of dictionaries, each representing a restaurant item

    Returns:
        None
    """
    for item in menu:
        print(f"{item['Item']}: ${item['Price']} ({item['Cal']} Cal)")

print_menu(taco_bell_menu)