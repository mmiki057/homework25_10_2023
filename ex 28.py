number = input('Enter EAN-13 article number: ')
if (number[:3] == '590') and (len(number) == 13):
    print('Article number is correct', 'Article manufactured in Poland', sep='\n')