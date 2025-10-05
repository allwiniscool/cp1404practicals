# question 1
FILENAME = "name.txt"
out_file = open(FILENAME, "w")
user_name = input("name: ")
print(user_name, file=out_file)
out_file.close()

# question 2
in_file = open(FILENAME, "r")
name = in_file.read().strip()
print(f"hi {name}!")
in_file.close()

# question 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())  # read first line
    number2 = int(in_file.readline())  # read second line
    total = number1 + number2
    print(total)

#question 4
total = 0
with open("numbers.txt", "r") as in_file:
    for number in in_file:
        total += int(number)
        print(total)