#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10 / 0
# TODO: Exceptions provide a way of catching errors and then handling them in
# a separate section of the code to group them together
try:
    x = 10 / 0
except:
    print("ERROR!!!!")

# TODO: You can also catch specific exceptions
try:
    answer = input("What should i divide 10 by ?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("ERROR!!!!")
except ValueError as e:
    print("Not valid number")
    print(e)
