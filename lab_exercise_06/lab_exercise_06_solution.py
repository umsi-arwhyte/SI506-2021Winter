# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
starbucks_menu = [
    ["Caramel Macchiato", 250],
    ["Chia Latte", 240],
    ["Flat White", 170],
    ["Chestnut Praline Latte", 330],
    ["Coffee Frapp", 230],
    ["Caramel Ribbon Crunch Frapp", 470],
    ["Matcha Green Tea Frapp", 420]
]

# END SETUP

# PROBLEM 1 (3 points)
def get_name(drink):
    return drink[0]

name = get_name(starbucks_menu[0])

print(f"\n1. First menu item: {name}")

# Problem 2A
def get_calories(drink):
    return drink[1]

calories = get_calories(starbucks_menu[1])

print(f"\n2A. Calories for second menu item: {calories}")

# Problem 2B
print('\n2B. Print strings:')
for drink in starbucks_menu:
    name = get_name(drink)
    calories = get_calories(drink)
    print(f"{name} has {calories} calories.")

# PROBLEM 3 (5 points)
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)

remove_menu_item(starbucks_menu, starbucks_menu[-1])

print(f"\n3. {starbucks_menu}")

# Problem 4 (6 points)

def add_menu_item(menu, item, position=0):
    menu.insert(position, item)

tea = ["Tea Latte", 100]
add_menu_item(starbucks_menu, tea, 3)

print(f"\n4. {starbucks_menu}")

# END LAB EXERCISE