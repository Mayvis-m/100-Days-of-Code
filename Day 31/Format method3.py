# str.format() = optional method that gives users
#                more control when displaying output

# number = 3.14159
number = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))          #makes a binary number
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))          #scientific notaition