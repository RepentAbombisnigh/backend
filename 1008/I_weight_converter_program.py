weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
#by adding .upper lower character can be identified as well
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your are {converted} kilos.")
else: 
    converted = weight / 0.45
    print(f"You are {converted} pounds.")