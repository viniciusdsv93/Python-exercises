# Program that calculates the double, the triple and the squareroot of a number entered by the user

from math import sqrt

number = int(input('Enter a number: '))

print("The double of the number {} is {}, the triple is {} and it's squareroot is {}".format(number, number * 2, number * 3, sqrt(number)))
