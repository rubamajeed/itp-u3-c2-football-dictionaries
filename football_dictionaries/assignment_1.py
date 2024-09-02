def players_as_dictionaries(squads_list):
    SQUADS_DICT = []

for player in SQUADS_DATA:
    player_dict = {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8],
    }
    SQUADS_DICT.append(player_dict)

# Output the result
print(SQUADS_DICT)

