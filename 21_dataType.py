# Program that prints the type of the data entered by the user

data = input('\nEnter anything: \n')
print(type(data))
print('Is it alphabetical? ', data.isalpha())
print('Is it numeric? ', data.isnumeric())
