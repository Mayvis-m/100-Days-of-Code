# key word arguments = arguments preceded by an identifier when we pass them to a function
#                      The order of the arguments doesn't matter, umlike positional arguments
#                       Python knows the names of the arguments that our function recieves

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last+ " ")

hello(last='Underscore', middle = 'Cyber', first = 'Mayvis')
