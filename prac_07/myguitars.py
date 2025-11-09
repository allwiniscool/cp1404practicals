from os import write

from guitar import Guitar

def main():
    guitars = []
    load_file(guitars)
    add_guitar(guitars)
    save_guitars(guitars)


def load_file(guitars):
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        row = [row.strip() for row in line.strip().split(",")]
        name = row[0]
        year = float(row[1])
        cost = float(row[-1])
        guitars.append(Guitar(name, year, cost))
    in_file.close()

def add_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        name = input("Name: ")
    guitars.sort()
    for guitar in guitars:
        print(guitar)



def save_guitars(guitars):
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar}\n")
        out_file.close()




main()





