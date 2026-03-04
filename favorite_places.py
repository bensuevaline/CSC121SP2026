favorite_places = {
    'Dasan': ['New Orleans'],
    'Janet': ['New York'],
    'Evaline': ['Salem']
}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite place is:")

    for place in places:
        print(place)