for number in range(1,101,+1):
    if number % 3 == 0:
        if number % 5 == 0:
            print('FizzBuzz')
            continue
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
