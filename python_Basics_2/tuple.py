#tuple

my_tuple = (1,2,3,4,5,5,5,5,5) # Hey Don't change it 
print(my_tuple[1])
print(5 in my_tuple)
user = {
        (1,2) : [1,2,3],
        'twitter' : '@Freyjst',
        'age' : 21
        }
print(user.items())
print(user[(1,2)])
my_tuple2 = (1,2,3,666,5)
new_tuple = my_tuple2[1:4]
print(new_tuple)
x,y,z, *zoro = (1,2,3,4,5,6)
print(zoro)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
