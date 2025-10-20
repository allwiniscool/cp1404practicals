
COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "Aquamarine1": "#7fffd4", "Asparagus": "#87a96b", "Barn Red": "#7c0a02",
                  "Bleu de France": "#318ce7", "Bright Green": "#66ff00"}


colour_name = input("Enter a colour name: ").strip()
while colour_name != "":
    if colour_name.lower() in [key.lower() for key in COLOUR_TO_CODE]:
        for name, code in COLOUR_TO_CODE.items():
            if colour_name.lower() == name.lower():
                print(f"The code for {name} is {code}")
    else:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").strip()

print("Goodbye!")
