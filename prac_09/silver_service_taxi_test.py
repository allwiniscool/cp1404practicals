from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("taxi1", 100, 2)
taxi.drive(18)
print(f"{taxi}, leads to a far cost of ${taxi.get_fare()}")
