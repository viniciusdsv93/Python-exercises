#Program that calculates the double, the triple and the squareroot of a number digited by the user.

from math import sqrt

number = int(input("Digit the number: "))

print("The double of the number {} is {}, the triple is {} and it's squareroot is {}".format(number, number * 2, number * 3, sqrt(number)))

#'O seu dobro é ',n*2,'o seu tripo é ',n*3,'e a sua raiz quadrada é ',n**(1/2))
