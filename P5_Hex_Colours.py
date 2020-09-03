hex_colours = {"aquamarine4": "#458b74", "azure3": "#c1cdcd", "black": "#000000", "blue2": "0000ee", "brown2": "ee3b3b", "chartreuse3": "66cd00", "darkorchid 4": "68228b", "floralwhite": "fffaf0", "gold1": "ffd700", "orangered2": "ee4000"}
print(hex_colours)
colour_choice = input("What colour do you want the hexadecimal code for? \n>>> ").lower()
while colour_choice not in hex_colours:
    print("Invalid colour choice ")
    colour_choice = input("What colour do you want the hexadecimal code for? \n>>> ").lower()
print(colour_choice, "is", hex_colours[colour_choice])



