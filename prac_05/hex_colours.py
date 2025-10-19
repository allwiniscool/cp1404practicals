
COLOUR_TO_CODE = {"AliceBlue": "#f0f8ff", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "Aquamarine1": "#7fffd4", "Asparagus": "#87a96b", "Barn Red": "#7c0a02",
                  "Bleu de France": "#318ce7", "Bright Green": "#66ff00"}

colour_name = input("Enter colour name: ").lower()


while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").lower()
