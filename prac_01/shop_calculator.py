number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
print(f"the total price of {number_of_items} is {total_price:.2f}")