for i in range (1, 31):
    if i%15==0:
        print('BINGO')
        continue
    elif i%3==0:
        print('THREE')
        continue
    elif i%5==0:
        print('FIVE')
        continue
    print(i)