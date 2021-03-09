# LAB EXERCISE 04
print('Lab Exercise 04 \n')

# Setup
grammy_winners = [
    ["Whitney Houston", "Pop", 6],
    ["Michael Jackson", "Pop", 19],
    ["Carrie Underwood", "Country", 7],
    ["Adell", "Soul", 15],
    ["Beyonce", "Pop", 20],
    ["Kendrick Lamar", "Hip-Hop", 12],
    ["Drake", "R&B Rap", 5]
    ]

# Problem 01 (3 points)

artist_names = []
for artist in grammy_winners:
    artist_names.append(artist[0])

print(f"\n1. Artist names = {artist_names}")

# Problem 02 (3 points)

pop_genre = []
for artist in grammy_winners:
    if artist[1].lower() == "pop":
        pop_genre.append(artist)

print(f"\n2. Pop genre = {pop_genre}")

# Problem 03 (4 points)

grammy_count_diff = 0
for artist in grammy_winners:
    if artist[-1] >= 15:
        grammy_count_diff += artist[-1]
    else:
        grammy_count_diff -= artist[-1]

print(f"\n3. Grammy count diff = {grammy_count_diff}")

# Problem 04 (5 points)

five_to_seven_grammies = []
for artist in grammy_winners:
    if 5 <= artist[-1] <= 7:
        five_to_seven_grammies.append(artist)

print(f"\n4. 5-7 Grammies = {five_to_seven_grammies}")

# Problem 05 (5 points)

top_artist = None
count = 0
for artist in grammy_winners:
    if artist[-1] > count:
        top_artist = artist[0]
        count = artist[-1]

print(f"\n5. Top artist = {top_artist}")