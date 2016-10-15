# Set cars variable
cars = 100
# Set space_in_a_car variable
space_in_a_car = 4.0
# Set drivers variable
drivers = 30
# Set passengers variable
passengers = 90
# Set cars_not_driven variable expression
cars_not_driven = cars - drivers
# Set cars_driven variable expression
cars_driven = drivers
# Set carpool_capacity variable expression
carpool_capacity = cars_driven * space_in_a_car
# Set average_passengers_per_car variable expression
average_passengers_per_car = passengers / cars_driven

# Print cars variable
print "There are", cars, "cars available."
# Print drivers variable
print "There are only", drivers, "drivers available."
# Print cars_not_driven variable
print "There will be", cars_not_driven, "empty cars today."
# Print carpool_capacity variable
print "We can transport", carpool_capacity, "people today."
# Print passengers variable
print "We have", passengers, "to carpool today."
# Print average_passengers_per_car variable
print "We need to put about", average_passengers_per_car, "in each car."


# The error occured on line 8 because the variable was typed incorrectly
