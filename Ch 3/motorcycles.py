motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replacing an element in a list 2
motorcycles[0] = 'ducati'
print(motorcycles)

# append (add to the list) 3
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# adding to a blank list 4
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)

# inserting an element
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing an elements (this case the second)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop
motorcycles = ['honda', 'yamaha', 'suszuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# how are pop useful
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f" The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)












