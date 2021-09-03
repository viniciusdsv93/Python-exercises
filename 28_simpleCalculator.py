# Simple calculator

a = float(input('Enter a number: '))
b = float(input('Enter another number: '))
c = input('Enter the operator, being + for addition, - for subtraction, * for multiplication and / for division: ')
if c == '+':
    d = a + b
    print('The sum between {} and {} equals {}.'.format(a,b,d))
elif c == '-':
    e = a - b
    print('The subtraction between {} and {} equals {}.'.format(a,b,e))
elif c == '*':
    f = a * b
    print('The multiplication between {} and {} equals {}.'.format(a,b,f))
elif c == '/':
    g = a / b
    print('The division between {} and {} equals {}.'.format(a,b,g))
else:
    print('Please, enter a valid operator.')
