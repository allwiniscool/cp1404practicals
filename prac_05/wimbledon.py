"""
CP1404/CP5632 Practical
Wimbledon champions data reader and processor

Estimated time: 30 minutes
Actual time: 78 minutes
"""


FILENAME = "wimbledon.csv"
def main():
    records = load_records()
    countries = extract_countries(records)
    champions_and_wins = extract_champions_and_wins(records)
    display_results(champions_and_wins, countries)

def load_records():
    """Load records from wimbledon.csv."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            clean_line = line.strip().replace("\t", ", ")
            records.append(clean_line.split(","))
    in_file.close()
    return records

def extract_champions_and_wins(records):
    """Extract champions and their wins from records."""
    champions_and_wins = {}
    for champion in records:
        if champion[2] in champions_and_wins:
            champions_and_wins[champion[2]] += 1
        else:
            champions_and_wins[champion[2]] = 1
    return champions_and_wins

def extract_countries(records):
    """Extract countries from records."""
    countries = set()
    for champion in records:
        countries.add(champion[1])
    return countries




def display_results(champions_and_wins, countries):
    """Display the champions and their wins as well as the countries that have won."""
    print("Wimbledon Champions: ")
    for champion, win in champions_and_wins.items():
        print(f"{champion} {win}")
    print("")
    print("These 12 countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()