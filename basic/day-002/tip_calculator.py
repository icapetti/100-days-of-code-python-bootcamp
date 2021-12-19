print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? ').replace('$', ''))
split_number = int(input('How many people to split the bill? '))
tip_percentage = float(input('What percentage tip would you like to give? 10, 12 or 15? '))

print(f'Each person should pay: ${(total_bill + total_bill*(tip_percentage/100))/split_number}')