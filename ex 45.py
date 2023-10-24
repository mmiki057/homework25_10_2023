b = int(input('Enter the number: '))
for i in range (1, b+1):
    for j in range (2, i):
        if i%j==0:
            break
    else:
        if i==1:
            continue
        else:
            print(f'Prime numbers: {i}')