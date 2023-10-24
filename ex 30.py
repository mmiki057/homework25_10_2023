time24 = input('Enter time (24-hour format): ')
if int(time24[:2]) > 12:
    print(f'Time in 12-hour format: {int(time24[:2])-12}:{int(time24[3:])} pm')