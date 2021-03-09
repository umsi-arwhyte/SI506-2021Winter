# START PROBLEM SET 04
print('PROBLEM SET 04 \n')

# Problem 01
print('\nProblem 1')

# SETUP

hip_hop_artists = ["Juice WRLD", "Roddy Ricch", "The Weeknd", "DaBaby", "Lil Baby"]

rock_artists = ["Panic! At The Disco", "Machine Gun Kelly", "Fleetwood Mac", "The Beatles", "twenty one pilots"]

country_artists = ["Luke Combs", "Kane Brown", "Maren Morris", "Jason Aldean", "Sam Hunt"]

# END SETUP

pop_artists = ["The Weeknd", "Dua Lipa", "Justin Bieber", "Harry Styles", "Lewis Capaldi"]

pop_artists.remove("Justin Bieber")
pop_artists.append("Post Malone")

genres = {
    "Country": country_artists,
    "Hip-Hop": hip_hop_artists,
    "Pop": pop_artists,
    "Rock": rock_artists
}

# Problem 02
print('\nProblem 2')

# SETUP

top_ten_artists = ("Post Malone", "The Weeknd", "Roddy Rich", "DaBaby", "Drake", "Juice WRLD", "Lil Baby", "Harry Styles", "Taylor Swift", "Pop Smoke")

# END SETUP

for artist in hip_hop_artists:
    if artist in top_ten_artists:
        print(f'{artist} topped the Hip-Hop/R&B charts as well as the overall charts in 2020!')
    else:
        print(f"{artist} topped the Hip-Hop/R&B charts in 2020!")

# Problem 03
print('\nProblem 3')

# SETUP

top_five_pop_songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd"
    },
    {
        "title": "Adore You",
        "artist": "Harry Styles"
    },
    {
        "title": "Circles",
        "artist": "Post Malone"
    },
    {
        "title": "Don't Start Now",
        "artist": "Dua Lipa"
    },
    {
        "title": "Break My Heart",
        "artist": "Dua Lipa"
    }
]

# END SETUP

dua_lipa_appearances = 0

for song in top_five_pop_songs:
    if song["artist"] == "Dua Lipa":
        dua_lipa_appearances += 1


# Problem 04
print('\nProblem 4')

# SETUP

top_twenty_five_songs = [
    {"title": "Blinding Lights", "artists": ["The Weeknd"]},
    {"title": "Circles", "artists": ["Post Malone"]},
    {"title": "The Box", "artists": ["Roddy Ricch"]},
    {"title": "Don't Start Now", "artists": ["Dua Lipa"]},
    {"title": "Rockstar", "artists": ["DaBaby", "Roddy Ricch"]},
    {"title": "Adore You", "artists": ["Harry Styles"]},
    {"title": "Life is Good", "artists": ["Future", "Drake"]},
    {"title": "Memories", "artists": ["Maroon 5"]},
    {"title": "The Bones", "artists": ["Maren Morris"]},
    {"title": "Someone You Loved", "artists": ["Lewis Capaldi"]},
    {"title": "Say So", "artists": ["Doja Cat"]},
    {"title": "I Hope", "artists": ["Gabby Barrett", "Charlie Puth"]},
    {"title": "Dance Monkey", "artists": ["Tones and I"]},
    {"title": "Savage", "artists": ["Megan Thee Stallion"]},
    {"title": "Roxanne", "artists": ["Arizona Zervas"]},
    {"title": "Intentions", "artists": ["Justin Bieber", "Quavo"]},
    {"title": "Everything I Wanted", "artists": ["Billie Eilish"]},
    {"title": "Roses", "artists": ["SAINt JHN"]},
    {"title": "Watermelon Sugar", "artists": ["Harry Styles"]},
    {"title": "Before You Go", "artists": ["Lewis Capaldi"]},
    {"title": "Falling", "artists": ["Trevor Daniel"]},
    {"title": "10,000 Hours", "artists": ["Dan + Shay", "Justin Bieber"]},
    {"title": "Ballin'", "artists": ["Mustard", "Roddy Ricch"]},
    {"title": "Blueberry Faygo", "artists": ["Lil Mosey"]},
    {"title": "Heartless", "artists": ["The Weeknd"]},
    {"title": "BOP", "artists": ["DaBaby"]},
]

artist_appearances = [
    {
        "artist": "DaBaby",
        "appearances": 0
    },
    {
        "artist": "Harry Styles",
        "appearances": 0
    },
    {
        "artist": "Justin Bieber",
        "appearances": 0
    },
    {
        "artist": "Lewis Capaldi",
        "appearances": 0
    },
    {
        "artist": "Roddy Ricch",
        "appearances": 0
    },
    {
        "artist": "The Weeknd",
        "appearances": 0
    },
]

# END SETUP

for song in top_twenty_five_songs:
    for artist in song["artists"]:
        if artist == 'DaBaby':
            artist_appearances[0]["appearances"] += 1
        elif artist == 'Harry Styles':
            artist_appearances[1]["appearances"] += 1
        elif artist == 'Justin Bieber':
            artist_appearances[2]["appearances"] += 1
        elif artist == 'Lewis Capaldi':
            artist_appearances[3]["appearances"] += 1
        elif artist == 'Roddy Ricch':
            artist_appearances[4]["appearances"] += 1
        elif artist == 'The Weeknd':
            artist_appearances[5]["appearances"] += 1


#Problem 05
print('\nProblem 5')

# SETUP

most_appearances = 0
artist_name = None

# END SETUP

for artist in artist_appearances:
    if artist["appearances"] > most_appearances:
        artist_name = artist["artist"]
        most_appearances = artist["appearances"]

print(f"{artist_name} appeared the most in the top 25 songs with {most_appearances} appearances.")
