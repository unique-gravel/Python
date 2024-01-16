weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if(unit.upper() == 'L'):
    coverted = weight / 0.45
    print(f"You are {coverted} pounds")
else:
    converted = weight * 0.45
    print(f"You are {converted} kilos")