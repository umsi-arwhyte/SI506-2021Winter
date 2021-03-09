# START PROBLEM SET 03
print('Problem Set 03')

# PROBLEM 1 (10 points)
print('\nProblem 1')
shijingshan = ('Big Air',)
zhangjiakou = ('Cross', 'Halfpipe', 'Parallel slalom', 'Slopestyle')
snowboarding_events = shijingshan + zhangjiakou

# PROBLEM 2 (10 points)
print('\nProblem 2')
sports = ["Luge", "Ice hockey", "Curling", "Skating", "Biathlon", "Bobsledding", "Skiing"]

sports_new = sports[-3:-1] + sports[2::-1] + sports[3:4]+ sports[-1:]
# PROBLEM 3 (20 points)
print('\nProblem 3')
skating_disciplines = "Figure skating|Short track speed skating|Speed skating"
skating_disciplines_list = skating_disciplines.lower().split("|")
events_count = [5,9,14]

figure_skating = {
    'name': skating_disciplines_list[0],
    'count': events_count[0]
}

short_track_speed_skating = {
    'name': skating_disciplines_list[1],
    'count': events_count[1]
}

speed_skating = {
    'name': skating_disciplines_list[2],
    'count': events_count[2]
}
# PROBLEM 4 (20 points)
print('\nProblem 4')
figure_skating['name'] = figure_skating['name'].replace(' ', '_').title()
short_track_speed_skating['count'] += 3
speed_skating.pop('count')



# PROBLEM  5 (20 points)
print('\nProblem 5')
sports_dict = {}

sports_dict["Skating"] = []

sports_dict["Skating"].append(figure_skating)
sports_dict["Skating"].append(short_track_speed_skating)
sports_dict["Skating"].append(speed_skating)

sports_dict['Skating'].pop()

# PROBLEM 6 (20 points)
print('\nProblem 6')
curling = {"Curling": [{"name": "Curling", "count": 3}]}
sports_dict.update(curling)
word_count = len(sports_dict['Skating'][0]['name'].split('_')) + len(sports_dict['Skating'][1]['name'].split(' ')) + 1
