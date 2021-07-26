# Program that calculates the amount of paint needed for a wall.

n1 = float(input('Enter the wall\'s width in meters = '))
n2 = float(input('Enter the wall\s height in meters = '))
area = float(n1*n2)

print(f'The total area is {area} m², wich is going to consume {float(area/2)} liters of paint.')
