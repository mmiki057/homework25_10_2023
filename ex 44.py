sum, quantity, amount = 0, 0, 1
while amount != 0:
    inp = int(input('Enter the number: '))
    amount = inp
    if amount == 0:
        break
    quantity += 1
    sum += inp
print(f'RESULT: Quantity = {quantity}, Sum = {sum}, Mean = {sum/quantity}')