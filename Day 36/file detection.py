import os

path = "C:\\Users\\marga\\OneDrive\\Desktop"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesn't exist!")
