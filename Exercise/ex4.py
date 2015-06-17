#number of cars
cars = 100
#seats in each car
space_in_a_car = 4
#how many drivers you have
drivers = 30
#how many passengers
passengers = 90

#calculate empty cars
cars_not_driven = cars - drivers
#change name for understanding
cars_driven = drivers

#calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#calculate average passengers per car.
average_passengers_per_car = passengers / cars_driven



print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."



#The problem with the original document was that the variable was not
#spelled correctly.

#1. To answer the question about why you put 4.0, it's so that 
#there will be a floating point value.

