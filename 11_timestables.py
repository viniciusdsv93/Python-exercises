# Program that calculates the times tables of a number entered by the user.

number = int(input("Enter the number: "))

"""print("{} * 1 = {}".format(number, number * 1))
print("{} * 2 = {}".format(number, number * 2))
print("{} * 3 = {}".format(number, number * 3))
print("{} * 4 = {}".format(number, number * 4))
print("{} * 5 = {}".format(number, number * 5))
print("{} * 6 = {}".format(number, number * 6))
print("{} * 7 = {}".format(number, number * 7))
print("{} * 8 = {}".format(number, number * 8))
print("{} * 9 = {}".format(number, number * 9))
print("{} * 10 = {}".format(number, number * 10))"""

i = 1

while i < 11:
    print("{} * {} = {}".format(number, i, number * i))
    i = i + 1
