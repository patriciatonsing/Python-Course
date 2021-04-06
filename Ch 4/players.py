players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[0:4])
print(players[:4])
# A slice that includes the end of a list
print(players[2:])
print(players[-3:])
print("here are the first players of my team:")
for player in players[:3]:
    print(player.title())

