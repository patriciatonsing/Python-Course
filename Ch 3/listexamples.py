# 36
print(3.1)
family = ['jerry', 'alma', 'maria']
for name in family:
    print(f"what do you want to eat, {name.title()}?")

#print(f"what do you want to eat, {family[1].title()}?")
#print(f"what do you want to eat, {family[2].title()}?")

# 42

print("Changing Guest list")
guests = ['Jackie Kennedy', 'Audrey Hepburn', 'Princess Diana']
print(f" Hi, {guests[0]} will you be available for my party?")

print(f"{guests[2]} wont be able to make it.")
guests[2] = 'Michelle Obama'
print(guests)

for guest in guests:
    print(f"Hi, {guest} you are invited to my dinner party.")
    print(f"We have found a bigger table")

guests.insert(0,'Joe Biden')
guests.insert(len(guests)//2, 'Patricia')
guests.append('Simon')
for guest in guests:
    print(f"Hi {guest} you are invited to my Party!")
print("We unfortunately can ony invite two persons")

while not len(guests) == 2:
    popped_guest = guests.pop()
    print(guests)
    print(popped_guest)
    print(f" Hi {popped_guest}, unfortunately you are not invited anymore. Sorry. Maybe next time. ")
for guest in guests:
    print(f" Hi, {guest} you are still invited to my party! Congrats!")
del guests[0:2]
print(guests)


# to figure what index is in the middle list
print(len(guests)//2)


