# START LAB EXERCISE 03
print('Lab Exercise 03 \n')

# PROBLEM 1 (5 Points)

inventors = {'Marie Van Brittan Brown': 'Home security system',
'Alice H. Parker': 'Furnace for central heating', 'Leonidas Berry':
'Gastroscope pioneer', 'Otis Boykin': 'Artificial heart pacemaker control unit',
'David Crosthwait': 'Heating' }

# END SETUP

# PROBLEM 2 (4 Points)
invention = 'Heating, ventilation, and air conditioning'

inventors['David Crosthwait'] = invention

# PROBLEM 3 (4 Points)

# SETUP
new_inventor = {'Alexander Miles': 'Automatic electric elevator doors'}

# END SETUP

inventors.update(new_inventor)

print(f'The updated inventor list: {inventors}')

# PROBLEM 4 (4 Points)
inventors.pop('Marie Van Brittan Brown')

print(f'The inventors in the list are: {inventors}')

# PROBLEM 5 (4 Points)

# SETUP
gastroscope_inventor = 'Leonidas Berry'

# END SETUP

tuple_gastroscope_inventor = (gastroscope_inventor,)

print(f'''The data type of < tuple_gastroscope_inventor >  is {type(tuple_gastroscope_inventor)} and\
 prints as {tuple_gastroscope_inventor}''')

# PROBLEM 6 (4 Points) 
medical_inventors = tuple_gastroscope_inventor + ('Otis Boykin',)

print(f'''Two inventors with medical related inventions: {medical_inventors}''')


# END LAB EXERCISE