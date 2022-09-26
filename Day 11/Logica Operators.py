# logical operators (and,or,not) = used to check if two or more conditional statements are true

# and, or operator
temp = int(input("what is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temerpature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temeprature is bad today!")
    print("Stay inside!")

# not operator 
temp = int(input("what is the temperature outside?: "))

if not (temp >= 0 and temp <= 30):
    print("The temeprature is bad today!")
    print("Stay inside!")
 
elif not (temp < 0 or temp > 30):
    print("The temerpature is good today!")
    print("Go outside!")
