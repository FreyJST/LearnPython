user = {
        'name':'Frey',
        'age':22,
        'sex':'Male',
        }
print(user['name'])
print(user is ['country'])
print(user.get('country'))

new_user = user

user.get('country', 505)

print(user)

print(new_user)

user2 = dict(name='FreyJST', age=55)

print(user2)
