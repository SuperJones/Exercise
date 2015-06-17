name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %i." % name
print "He's %x inches tall." % height
print "He's %i pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

height_cm = height / 0.39370
print height_cm

weight_kg = weight / 2.2046
print weight_kg


