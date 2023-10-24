car_speed, speed_limit_min, speed_limit_max = int(input('Enter the car speed: ')), 40, 140
if (speed_limit_max < car_speed) or (car_speed < speed_limit_min):
    print('Warning: invalid car speed!!')