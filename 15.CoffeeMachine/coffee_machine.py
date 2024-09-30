import dictionary
import art

# Initial machine ingredients
machine_ingredients = {
    'water': 1000,
    'coffee': 500,
    'milk': 1000,
    'sugar': 500
}


def begin():
    print(art.machine)

    # Select coffee by name or number
    coffee_choice = input('What coffee do you want? (name or number): ').strip().lower()

    coffee_names = list(dictionary.coffee_menu.keys())

    # Handle number input
    if coffee_choice.isdigit():
        coffee_index = int(coffee_choice) - 1
        if 0 <= coffee_index < len(coffee_names):
            coffee_choice = coffee_names[coffee_index]  # Convert number to coffee name
        else:
            print("Invalid selection, please try again.")
            begin()  # Restart coffee selection
            return

    if coffee_choice not in coffee_names:
        print("We don't have that kind of coffee!")
        begin()  # Restart coffee selection
    else:
        coffee_maker(coffee_choice)


def coffee_maker(coffee_choice):
    coffee_needed_ingredients = dictionary.coffee_menu[coffee_choice]['ingredients']

    global machine_ingredients
    # Check if machine has enough ingredients
    if all(machine_ingredients.get(ingr, 0) >= amount for ingr, amount in coffee_needed_ingredients.items()):
        # Deduct ingredients and proceed to coin payment
        for ingr, amount in coffee_needed_ingredients.items():
            machine_ingredients[ingr] -= amount
        coins_needed(coffee_choice)
    else:
        print('Not enough ingredients for this coffee. Please try another:')
        begin()


def coins_needed(coffee_choice):
    coffee_price = dictionary.coffee_menu[coffee_choice]['price']
    print(f'Your coffee costs: {coffee_price} CHF')

    while True:  # Use a loop to handle insufficient funds without recursion
        # Input for coins
        five_rappen = int(input('How many 5 rappen coins?: ')) * 0.05
        ten_rappen = int(input('How many 10 rappen coins?: ')) * 0.10
        twenty_rappen = int(input('How many 20 rappen coins?: ')) * 0.20
        fifty_rappen = int(input('How many 50 rappen coins?: ')) * 0.50
        one_franc = int(input('How many 1 franc coins?: ')) * 1.00
        two_franc = int(input('How many 2 franc coins?: ')) * 2.00
        five_franc = int(input('How many 5 franc coins?: ')) * 5.00

        coins_put = five_rappen + ten_rappen + twenty_rappen + fifty_rappen + one_franc + two_franc + five_franc

        if coins_put >= coffee_price:
            print('Your coffee is being made...')
            change = round(coins_put - coffee_price, 2)

            # Calculate change
            coins_change = {}
            for coin, details in sorted(dictionary.franc_coins.items(), key=lambda x: -x[1]['value']):
                coin_value = details['value']
                if change >= coin_value:
                    coins_needed = int(change // coin_value)
                    coins_change[coin] = coins_needed
                    change = round(change % coin_value, 2)

            # Display change in a clean format
            if coins_change:
                print("Your change is:")
                for coin, count in coins_change.items():
                    print(f"{count} x {coin} coins")
            else:
                print("No change is due.")

            ask_another_coffee()  # Ask if the user wants another coffee
            break  # Exit the loop since the coffee is being made
        else:
            print(f'Insufficient funds! You entered {coins_put} CHF but need {coffee_price} CHF.')
            print('Please try again.')


def ask_another_coffee():
    another_coffee = input("Would you like another coffee? (y/n): ").lower().strip()
    if another_coffee == 'y':
        begin()  # Restart the process
    elif another_coffee == 'n':
        print("Thank you for using the coffee machine! Goodbye!")
        exit()
    else:
        print("Invalid input, please try again.")
        ask_another_coffee()  # Repeat until valid input


print("Welcome to the Coffee Machine!")
begin()
