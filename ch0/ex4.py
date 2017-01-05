# There are 100 cars.
cars = 100
# The car has 4 seats.
space_in_a_car = 4.0
# There are 30 drivers.
drivers = 30
# There are 90 passengers .
passengers = 90
# The number of all cars minus the number of drivers is the number of not-driven cars .
cars_not_driven = cars - drivers 
# The number of driven cars is the number of drivers 
cars_drivern =drivers
# The number of carpool capacity is multiplied by the number of the driven cars and the space in car .
carpool_capacity = cars_drivern * space_in_a_car
# The average passengers of per car is divided by the number of passengers and driven cars.
average_passengers_per_car = passengers / cars_drivern


print("There are", cars ,"cars available.")
print("There are only", drivers, "drivers available.")
print("There will be ",cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car ,"in each car.")