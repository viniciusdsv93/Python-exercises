# Program that converts an amount of seconds in days, hours, minutes and seconds

seconds = int(input('Enter the number of seconds: '))
days = seconds // 86400
secondsRest = seconds % 86400
hours = secondsRest // 3600
secondsRest = secondsRest % 3600
minutes = secondsRest // 60
secondsRest = secondsRest % 60
print(days,'days,',hours,'hours,',minutes,'minutes and',secondsRest,'seconds.')
