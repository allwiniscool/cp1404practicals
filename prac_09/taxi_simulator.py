from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive
>>> """

def main():
    """The main function takes input and gives users result based on input shown on menu."""
    bill_to_date = 0
    chosen_taxi = ""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            chosen_taxi = choose_taxi(taxis)

        elif choice == "d":
            bill_to_date = drive_taxi(taxis, chosen_taxi, bill_to_date)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date}")
        choice = input(MENU).lower()
    print(f"Total trip cost: ${bill_to_date}")
    for i, taxi in enumerate(taxis):
        print(i, taxi)

def choose_taxi(taxis):
    """Choose a taxi from the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(i, taxi)
    choice = get_valid_number("Choose taxi: ")
    while choice >= len(taxis) or choice < 0 :
        print("Invalid taxi choice")
        choice = ""
        return choice
    return int(choice)

def drive_taxi(taxis, chosen_taxi, bill_to_date):
    """Drive a taxi from the chosen taxi."""
    if chosen_taxi == "":
        print("You need to choose a taxi before you can drive")
        return bill_to_date
    taxi = taxis[int(chosen_taxi)]
    if taxi.fuel == 0:
        print("No fuel left.")
        return bill_to_date
    else:
        distance = get_valid_number(prompt= "Drive how far? ")
        taxi.drive(distance)
        print(taxi)
        trip_cost = taxi.get_fare()
        bill_to_date += trip_cost
        print(f"Your {taxi.name} trip cost you ${trip_cost}")
        return bill_to_date



def get_valid_number(prompt = ""):
    """Get a valid number from user input."""
    while True:
        try:
            choice = int(input(prompt).strip())
            return choice
        except ValueError:
            print("Invalid input")

main()
