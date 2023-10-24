pin, possibilities = '0805', 3
for _ in range (3):
    entering = input('Enter the PIN: ')
    if entering != pin:
        if possibilities != 0:
            possibilities -= 1
            print('Incorrect...')
        else:
            print('Incorrect...', 'Sorry, your payment card has been blocked.', sep='\n')
    else:
        print('Payment succesful!')
        break
