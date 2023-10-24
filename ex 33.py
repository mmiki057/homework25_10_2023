decimal_number = int(input('Enter the decimal number: '))
decimal_number_dividing = decimal_number
binary_number = ''
while decimal_number_dividing != 0:
    binary_number += str(decimal_number_dividing%2)
    decimal_number_dividing //= 2
print(f'{decimal_number}(10) = {binary_number[::-1]}(2)')
