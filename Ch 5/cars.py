# only bmw must be in all uppercase
cars = ['audi', 'bmw', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# conditional tests
car = 'audi'
print(car == 'bmw')

print(car == 'Audi')
print(car.lower() == 'audi')
car






