bill_price = float(input("What is your bill price?: $"))
tip_size = int(input("How much tip would you like to give?: 10%, 12% or 15%: "))
people = int(input("How many people are splitting the bill?: "))

tip_procent = 0.0

if tip_size == 10:
    tip_procent = 1.1
elif tip_size == 12:
    tip_procent = 1.12
elif tip_size == 15:
    tip_procent = 1.15
else:
    print("This tip doesn't exist in our restaurant")

price_per_person = (bill_price * tip_procent)/people

print(f"Your bill is ${price_per_person:.2f}")
