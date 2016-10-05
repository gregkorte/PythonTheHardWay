name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
heightToCentimeters = height * 2.54
weightToKilograms = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height, heightToCentimeters)
print "He's %d pounds or %d kilograms heavy." % (weight, weightToKilograms)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
