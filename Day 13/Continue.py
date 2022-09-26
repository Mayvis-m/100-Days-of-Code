# CONTINUE
phone_number = "555-555-5555"

for index in phone_number:
    if index == "-":
        continue
    print(index, end="")