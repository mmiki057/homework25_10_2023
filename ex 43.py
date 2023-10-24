a1, a2 = 0, 1
print('0', end =' ')
for i in range (19):
    a1, a2 = a2, a2 + a1
    print(a1, end=' ')