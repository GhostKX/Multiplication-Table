# Multiplication Table
while True:
    number = input('Type in any number to calculate or "0" to exit: ')
    if number.lstrip('-').isdigit() or number.lstrip('+').isdigit():
        number = int(number)
        if number == 0:
            print('\nExit')
            exit(0)
        else:
            print('\nTable of multiplication for number "{}":'.format(number))
            for i in range(1, 11):
                output = number * i
                print(f'{number} * {i} = {output}')
            print()
    elif number.isalpha():
        print('\nError unknown symbol\n')








