current, previous = float(input('Current product price: ')), float(input('Previous product price: '))
reduce = (previous-current)/previous*100
if reduce >= 10:
    print('Buy the product!!', f'Product price reduced by {reduce}%')
