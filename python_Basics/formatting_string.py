#
#Amazon login page

name = 'Frey'
#which amazon will store in db
age = 22

"""
print('hi ' + name + '. you are ' + str(age) + ' year old.')
"""
# let's use formatted string
print(f'hi {name}. you are {age} year old')

print('hi {}. you are {} year old'.format('yuichi', '18'))

print('hello there {1}, your age is {0}' .format('sanji', '24'))

#lol this will do some changes in ages and name !

print('hello there {new_name}, nice to meet you ! you are {new_age} year old .'.format(new_name='Frey', new_age=21))
