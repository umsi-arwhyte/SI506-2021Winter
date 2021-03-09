# START PROBLEM SET 05
print('Problem Set 05')
mens_champions = [
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2015},
    {'Champion': 'Stan Wawrinka','Country': 'SUI','Major': 'french open','Seed': 8,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 1,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'us open','Seed': 1,'Year': 2015},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2016},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'french open','Seed': 1,'Year': 2016},
    {'Champion': 'Andy Murray','Country': 'GBR','Major': 'wimbledon','Seed': 2,'Year': 2016},
    {'Champion': 'Stan Wawrinka','Country': 'SUI','Major': 'us open','Seed': 3,'Year': 2016},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'australian open','Seed': 17,'Year': 2017},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 4,'Year': 2017},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'wimbledon','Seed': 3,'Year': 2017},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'us open','Seed': 1,'Year': 2017},
    {'Champion': 'Roger Federer','Country': 'SUI','Major': 'australian open','Seed': 2,'Year': 2018},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 1,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 12,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'us open','Seed': 6,'Year': 2018},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'australian open','Seed': 1,'Year': 2019},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'french open','Seed': 2,'Year': 2019},
    {'Champion': 'Novak Djokovic','Country': 'SRB','Major': 'wimbledon','Seed': 1,'Year': 2019},
    {'Champion': 'Rafael Nadal','Country': 'ESP','Major': 'us open','Seed': 2,'Year': 2019}
 ]

womens_champions = [
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'australian open','Seed': 1,'Year': 2015},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'french open','Seed': 1,'Year': 2015},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'wimbledon','Seed': 1,'Year': 2015},
    {'Champion': 'Flavia Pennetta','Country': 'ITA','Major': 'us open','Seed': 26,'Year': 2015},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'australian open','Seed': 7,'Year': 2016},
    {'Champion': 'Garbiñe Muguruza','Country': 'ESP','Major': 'french open','Seed': 4,'Year': 2016},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'wimbledon','Seed': 1,'Year': 2016},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'us open','Seed': 2,'Year': 2016},
    {'Champion': 'Serena Williams','Country': 'USA','Major': 'australian open','Seed': 2,'Year': 2017},
    {'Champion': 'Jeļena Ostapenko','Country': 'LAT','Major': 'french open','Seed': 0,'Year': 2017},
    {'Champion': 'Garbiñe Muguruza','Country': 'ESP','Major': 'wimbledon','Seed': 14,'Year': 2017},
    {'Champion': 'Sloane Stephens','Country': 'USA','Major': 'us open','Seed': 0,'Year': 2017},
    {'Champion': 'Carolina Wozniacki','Country': 'DEN','Major': 'australian open','Seed': 2,'Year': 2018},
    {'Champion': 'Simona Halep','Country': 'ROU','Major': 'french open','Seed': 1,'Year': 2018},
    {'Champion': 'Angelique Kerber','Country': 'GER','Major': 'wimbledon','Seed': 11,'Year': 2018},
    {'Champion': 'Naomi Osaka','Country': 'JPN','Major': 'us open','Seed': 20,'Year': 2018},
    {'Champion': 'Naomi Osaka','Country': 'JPN','Major': 'australian open','Seed': 4,'Year': 2019},
    {'Champion': 'Ashleigh Barty','Country': 'AUS','Major': 'french open','Seed': 8,'Year': 2019},
    {'Champion': 'Simona Halep','Country': 'ROU','Major': 'wimbledon','Seed': 7,'Year': 2019},
    {'Champion': 'Bianca Andreescu','Country': 'CAN','Major': 'us open','Seed': 15,'Year': 2019}
 ]
# PROBLEM 1 (20 points)
print('\nProblem 1')
dark_horse_seed = 0
dark_horse = None
for champion_info in womens_champions:
    if champion_info["Seed"] > dark_horse_seed:
        dark_horse_seed = champion_info["Seed"]
        dark_horse = champion_info["Champion"]
print(dark_horse, dark_horse_seed)

# PROBLEM 2 (20 points)
print('\nProblem 2')
USOpen_native_winners = []
for champion_info in womens_champions:
    if champion_info["Country"] == "USA" and champion_info["Major"] == "us open":
        USOpen_native_winners.append(champion_info["Champion"])
print(USOpen_native_winners)

# PROBLEM 3 (20 points)
print('\nProblem 3')
mens_champions_times = {}
for champion_info in mens_champions:
    name = champion_info["Champion"]
    if name not in mens_champions_times:
        mens_champions_times[name] = 0
    mens_champions_times[name] += 1
print(mens_champions_times)

# PROBLEM 4 (20 points)
print('\nProblem 4')
most_GS_times = 0
most_GS_champion = None

for name, times in mens_champions_times.items():
    if times > most_GS_times:
        most_GS_champion = name
        most_GS_times = times
print(most_GS_champion, most_GS_times)

# PROBLEM  5 (20 points)
print('\nProblem 5')
womens_AO_times = {}
for champion_info in womens_champions:
    if champion_info["Major"] == 'australian open':
        name = champion_info["Champion"]
        if name not in womens_AO_times:
            womens_AO_times[name] = 0
        womens_AO_times[name] += 1
print(womens_AO_times)
most_AO_champion = None
most_AO_times = 0
for name, times in womens_AO_times.items():
    if times > most_AO_times:
        most_AO_champion = name
        most_AO_times = times
print(most_AO_champion, most_AO_times)