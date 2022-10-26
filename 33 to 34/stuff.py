
first_name = "Mayvis"
last_name = "Underscore"
full_name = first_name +" " + last_name

age = 100
human = True
height = 700.0

print("Hello, my name is " + full_name + "." " I am " + str(age) + ".")
print("Yes, it is "+ "'" +str(human)+ "'" " that I am human.")
print("My height is " +str(height)+" cm.")

drinks = ["iced coffee", "coke", "water","green tea"]
food = ["pizza","cheeseburgers","cheese sticks"]

print("Here are my favorite foods and drinks: ") 
print(food,drinks)

print(" ")

print("Let me get to know you now.")

print(" ")

while True:
    your_name = input("What is your name?: ")
    your_age = input("How old are you?: ")
    your_height = input("How tall are you?: ")
    drink_item = input("What do you like to drink?: ")
    food_item = input("What do you like to eat?: ")

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break

print("Your name is " + your_name + ".")
print("Your age is "+ str(your_age) + ".")
print("Your height is "+ str(your_height) + "cm.")
print("You like to drink " + drink_item + ".")
print("You like to eat "+ food_item + ".")
