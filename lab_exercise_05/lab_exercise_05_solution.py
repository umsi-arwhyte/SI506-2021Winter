# LAB EXERCISE 05
print('Lab Exercise 05 \n')

# SETUP
pop_tv_shows = [
    {"Title": "WandaVision", "Creator": ["Jac Schaeffer"], "Rating": 8.2, "Genre": "Action"},
    {"Title": "Attack on Titan", "Creator": ["Hajime Isayama"], "Rating": 8.9, "Genre": "Animation"},
    {"Title": "Bridgerton", "Creator": ["Chris Van Dusen"], "Rating": 7.3, "Genre": "Drama"},
    {"Title": "Game of Thrones", "Creator": ["David Benioff", "D.B. Weiss"], "Rating": 9.3, "Genre": "Action"},
    {"Title": "The Mandalorian", "Creator": ["Jon Favreau"], "Rating": 8.8, "Genre": "Action"},
    {"Title": "The Queen's Gambit", "Creator": ["Scott Frank", "Allan Scott"], "Rating": 8.6, "Genre": "Drama"},
    {"Title": "Schitt's Creek", "Creator": ["Dan Levy", "Eugene Levy"], "Rating": 8.5, "Genre": "Comedy"},
    {"Title": "The Equalizer", "Creator": ["Andrew W. Marlowe", "Terri Edda Miller"], "Rating": 4.3, "Genre": "Action"},
    {"Title": "Your Honor", "Creator": ["Peter Moffat"], "Rating": 7.9, "Genre": "Crime"},
    {"Title": "Cobra Kai", "Creator": ["Jon Hurwitz", "Hayden Schlossberg", "Josh Heald"] , "Rating": 8.6, "Genre": "Action"}
    ]

# END SETUP

# Problem 01 (4 points)
print('/nProblem 01')

action_shows = []

for show in pop_tv_shows:
    if show['Genre'] == 'Action':
        action_shows.append(show['Title'])

print(f'Action show list:{action_shows}')

# Problem 02 (4 points)
print('/nProblem 02')

high_rating = 0
highest_rated_show = None

for show in pop_tv_shows:
    if show["Rating"] > high_rating:
        high_rating = show["Rating"]
        highest_rated_show = show["Title"]

print(f'Highest rated show is {highest_rated_show} with a rating of {high_rating}')

# Problem 03 (4 points)
print('/nProblem 03')

low_rating = 10
lowest_rated_show = None

for show in pop_tv_shows:
    if show["Rating"] < low_rating and show['Genre'] != "Action":
        low_rating = show["Rating"]
        lowest_rated_show = show["Title"]

print(f'Lowest rated non-action show is {lowest_rated_show} with a rating of {low_rating}')

# Problem 04 (4 points)
print('/nProblem 04')

multiple_creators = []

for show in pop_tv_shows:
    if len(show["Creator"]) > 1:
        multiple_creators.append(show["Title"])

print(f'Show with multiple creators: {multiple_creators}')

# Problem 05 (4 points)
print('/nProblem 05')

show_genre = []

for show in pop_tv_shows:
    if show['Genre'] not in ["Action", "Drama"] or show["Rating"] >= 9:
        item = {'Title': show['Title'], 'Genre': show['Genre']}
        show_genre.append(item)

print(f'Show and genre: {show_genre}')