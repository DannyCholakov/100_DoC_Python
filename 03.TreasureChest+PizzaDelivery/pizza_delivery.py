print('Welcome to Python Pizza Delivery')
size = input('What size pizza do you want? S, M or L: ')
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

pizza_price = 0
if size == 'S':
    pizza_price += 15
elif size == 'M':
    pizza_price += 20
elif size == 'L':
    pizza_price += 25

if pepperoni == 'Y' and size == 'S':
    pizza_price += 2
else:
    pizza_price += 3

if extra_cheese == 'Y':
    pizza_price += 1

print(f'Your pizza price is ${pizza_price:.2f}')