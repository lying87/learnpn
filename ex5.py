name = 'Zed A. Shaw'
age = 35 # not a lie 
height = 74 # inches
weight =180 # 1bs
eye = 'Blue'
teech = 'White'
hair = 'Brown'
centimeter = 2.54  # inches
real_height  = height * centimeter
kilogram  = 2.204  # 1bs
real_weight = weight * kilogram 

print "Let's talk about %s." % name
print "He's %d centimeter tall." % real_height
print "He's %d kilogram heavy." % real_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eye, hair)
print "His teeth are usually %s depending on the coffee." % teech

# this line is tricky , try to get it exactly right
print "If I add %d , %d , and  %d I get %d ." % (
       age, real_height, real_weight, age + real_height + real_weight) 