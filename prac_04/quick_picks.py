import random

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 45)
        if number not in numbers:
            numbers.append(number)
    lines = ' '.join(f"{str(number):>2}" for number in sorted(numbers))
    print(lines)
