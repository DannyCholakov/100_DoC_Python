def new_calculation():
    first_number = int(input('Whats the first number?: '))
    start_operation(first_number)

def start_operation(first_number):
    operation = input("+\n-\n*\n/\nPick an operation: ")
    if operation == '+':
        add(first_number)
    elif operation == '-':
        sub(first_number)
    elif operation == '*':
        multi(first_number)
    elif operation == '/':
        divide(first_number)
    else:
        print("Wrong Input!")

def add(first_number):
    second_number = int(input('Whats the second number?: '))
    result = first_number + second_number
    print(f"The result of the operation is: {result}")
    continue_operation(result)

def sub(first_number):
    second_number = int(input('Whats the second number?: '))
    result = first_number - second_number
    print(f"The result of the operation is: {result}")
    continue_operation(result)

def multi(first_number):
    second_number = int(input('Whats the second number?: '))
    result = first_number * second_number
    print(f"The result of the operation is: {result}")
    continue_operation(result)

def divide(first_number):
    second_number = int(input('Whats the second number?: '))
    result = first_number / second_number
    print(f"The result of the operation is: {result}")
    continue_operation(result)

def continue_operation(result):
    calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if calculation == 'y':
        start_operation(result)
    elif calculation == 'n':
        new_calculation()
    elif calculation == 'end':
        exit()

new_calculation()