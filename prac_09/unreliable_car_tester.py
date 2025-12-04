from prac_09.unreliable_car import UnreliableCar

w = 0
l = 0
for i in range(0, 100):

    car = UnreliableCar(f"car{i}", 100, 30)
    car.driven(55)
    car_value = print(car)
    value = str(car_value).split()
    if value[-1] == "55":
        w += 1
    else:
        l += 1
print(w)
print(l)
