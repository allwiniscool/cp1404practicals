def main ():
    numbers = []
    for i in range(0, 5):
        input_number = int(input("Number: "))
        numbers.append(input_number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers)/len(numbers)
    print(f"The average of the numbers is {average:.2f}")

main()

