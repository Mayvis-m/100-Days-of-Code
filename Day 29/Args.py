# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#         you can replace args with any name as long as it has *
#         ex. *stuff instead of *args

def add(*mysoul):
    sum = 0
    mysoul = list(mysoul)
    mysoul[0] = 0
    for i in mysoul:
        sum += i
        
    return sum

print(add(1,2,3,4,5,6))
