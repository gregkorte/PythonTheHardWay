# Set x to a string with a digit variable
x = "There are %d types of people." % 10
# Set binary to a string
binary = "binary"
# Set do_not to a string
do_not = "don't"
# Set y to a string with two string variables (1,2)
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x variable
print x
# Print y variable
print y

# Print string with x variable (3)
print "I said: %r." % x
# Print string with y variable (4)
print "I also said: '%s'." % y

# Set hilarious to boolean
hilarious = False
# Set joke_evaluation to a string with a variable that will return valid python syntax
joke_evaluation = "Isn't that joke so funny?! %r"

# Print String using hilarious for the repr() (False)
print joke_evaluation % hilarious

# Set w to a string
w = "This is the left side of..."
# Set e to a string
e = "a string with a right side."

# Print the two concatenated strings
print w + e
