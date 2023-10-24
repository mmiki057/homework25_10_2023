time = 0
washing_product = "shoes"
rinse = True
spin = False
if washing_product == "shoes":
    time += 20
elif washing_product == "jacket":
    time += 40
elif washing_product == "underwear":
    time += 70
if rinse:
    time += 15
elif spin:
    time += 9
print(f'Total washing time: {time} minutes')