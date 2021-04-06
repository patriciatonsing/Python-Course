# 4-1 56
pizzas = 'mushroom', 'pineapple', 'cheese'
for pizza in pizzas:
    print(pizza)
print("I love homemade pizza from Trader Joe's. I really love pizza!")
# 4-2
animals = 'panda', 'penguin', 'bats'
for animal in animals:
    print(animal)
print(f"{animals[0]}s are soft")
print(f"{animals[1]} are very fast swimmers")
print(f"{animals[2]} are nocturnal animals")
print("All of these animals are black")

# 4 -3 60
for i in range(1,20):
    print(i)
# 4-4
#for i in range(1, 1000001):
   # print(i)

# 4-5 Summing a million
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6 Odd numbers
for i in range(1, 11, 2):
    print('This will print only odd numbers:', i)

# 4 - 7 Make a list of the multiples of 3 from 2 to 30. Use a for loop to print the numbers in your list
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# 4 - 8 A number raised to third power is called a cube.
cubes = []
for number in range(1,11):
    cube = number **3
    cubes.append(cube)

# 4- 9 Use a list comprehension to generate a list of the first 10 cubes
cubes = [number**3 for number in range (1,11)]
for cube in cubes:
    print(cube)



