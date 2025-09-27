MENU =("""(G)et valid score
(P)rint result
(S)how stars
(Q)uit""")

def main():
    """Get valid score and determine what to do based on choice made by the user."""
    score = get_valid_score(low=0, high=100, text="invalid score")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(low=0, high=100, text="invalid score")
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            stars = int(score) * "*"
            print(stars)
        else:
            print("invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("farwell")

def get_valid_score(low, high, text):
    """Get valid score."""
    score = float(input("score: "))
    while score > high or score < low:
        print(text)
        score = float(input("score: "))
    return score

def determine_result(score):
    """Determine grade based on score."""
    if score < 0 or score > 100:
        return ("Invalid score")
    elif score >= 90:
        return ("Excellent")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")

main()