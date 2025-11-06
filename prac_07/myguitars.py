

from guitar import Guitar

guitars = []
in_file = open('guitars.csv', 'r', newline='')
for line in in_file:
    row = [row.strip() for row in line.strip().split(",")]
    name = row[0]
    year = int(row[1])
    cost = float(row[-1])
    guitars.append(Guitar(name, year, cost))
guitars.sort()
for guitar in guitars:
    print(guitar)



