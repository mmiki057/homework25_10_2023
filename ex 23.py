age = int(input('Enter the dog\'s age: '))
if 0<= age <= 2:
    print(f'The dog\'s age in dog’s years is {age*10.5} years.') 
elif age > 2:
    print(f'The dog\'s age in dog’s years is {21+(age-2)*4} years.')
elif age < 0:
    print('Error')