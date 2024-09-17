import random

print("Welcome to Password Generator")
number_of_letter = int(input("How many letters would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))

letters_List = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_List = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_List = ['!', '@', '#', '$', '%', '^', '&']

password = []

# Add letters to the password
for _ in range(number_of_letter):
    char = random.choice(letters_List)
    password.append(char)

# Add numbers to the password
for _ in range(number_of_numbers):
    char = random.choice(numbers_List)
    password.append(char)

# Add symbols to the password
for _ in range(number_of_symbols):
    char = random.choice(symbols_List)
    password.append(char)

# Shuffle the password list to randomize the order
random.shuffle(password)

# Join the list into a string to form the final password
new_password = ''.join(password)
print(f"Your generated password is: {new_password}")
