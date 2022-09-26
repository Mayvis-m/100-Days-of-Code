# tuple = collection which is ordered and unchangable
#          used to group together related data

student = ("Mayvis", 35, "female")

# counts how many times Mayvis appears
print(student.count("Mayvis"))
# finds the index of female
print(student.index("female"))

# display all of the contents within a tuple using a for loop

for x in student:
    print(x)

if "Mayvis" in student:
    print("Mayvis is here!")