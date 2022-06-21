birth_year = input('what is your birth year ?:-')
real_age = (2022 - int(birth_year))
if (real_age >= 18):
	print('your age is :-' + str(real_age))
	print("yeah you can fuck")
else:
	print(f'your age is :- {real_age}')
	print('you are now a minor and your age is {} so you can\'t fuck'.format(real_age))
