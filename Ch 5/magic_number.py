answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again","\n")

age = 19
print(age < 21)
print(age <= 21,"\n")

# checking whether two conditions are both true simultaneously
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 > 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# to improve readability
print((age_0 >= 21) and (age_1 >= 21))

# Using or to check multiples
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 > 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# checking to see if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)






