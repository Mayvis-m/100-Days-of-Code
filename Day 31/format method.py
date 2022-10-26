# str.format() = optional method that gives users
#                more control when displaying output

adverb = "why"
noun = "house"

# print("This is "+adverb+" I don't leave the "+noun)

# print("This is {} I don't leave the {}".format(adverb,noun))
# print("This is {0} I don't leave the {1}".format(adverb,noun))  #positional argument
# print("This is {adverb} I don't leave the {noun}".format(adverb = "why",noun = "house"))    #keyword argument

text = "This is {} I don't leave the {}"
print(text.format(adverb,noun))
