#Oh, so instead of writing the string out, we made the string
# a variable and like normal, followed it with the 
# % and the replacements.
formatter = "%r %r %r %r"

#this is like printing the first and second half. But the 
# first half is the same so we used a variable instead. 
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

#The formatter is just a variable that stands for a string.
#Since the formatter is a string it can also be used where %r is.
print formatter % (formatter, formatter, formatter, formatter)

#this prints a very long string.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#--Mistakes--
#I got the distracted and missed the formatter formatter line.
