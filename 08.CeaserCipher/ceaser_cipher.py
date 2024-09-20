import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def command_prompt():
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    command = input().lower()
    if command == 'encode':
        encode_command()

    elif command == 'decode':
        decode_command()

def encode_command():
    print('Type your message:')
    message = input().lower()
    print('Type the shift number:')
    shift = int(input())
    encrypt(message, shift)
    print('Do you want to cipher again?: Yes/No')
    answer = input().lower()
    if answer == 'yes':
        command_prompt()
    else:
        exit()

def decode_command():
    print('Type the message:')
    message = input().lower()
    print('Type the shift number:')
    shift = int(input())
    decrypt(message, shift)
    print('Do you want to cipher again?: Yes/No')
    answer = input().lower()
    if answer == 'yes':
        command_prompt()
    else:
        exit()

def encrypt(message, shift):
    new_message = ''
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index + shift
            new_letter_index %= len(alphabet)
            new_message += alphabet[new_letter_index]
        else:
            new_message += letter
    print(new_message)

def decrypt(message, shift):
    new_message = ''
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter_index = letter_index - shift
            new_letter_index %= len(alphabet)
            new_message += alphabet[new_letter_index]
        else:
            new_message += letter
    print(new_message)

print(art.logo)
command_prompt()
