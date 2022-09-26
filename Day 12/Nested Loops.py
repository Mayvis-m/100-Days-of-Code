# nested loops = The "inner loop" will finish all of it's iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# OUTER LOOP = rows
# INNER LOOP = columns 

for index in range(rows):
    for j in range(columns): 
        print(symbol, end="")
    print()