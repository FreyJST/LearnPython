# finally the last DS
my_list = [1,2,3,4,5,6,7,8.4,6]
my_set = {1,2,3,4,5,2,3,4}
#there will be only unique items 
my_set.add(100)
my_set.add(3)
print(my_set)
print(set(my_list))
new_set = my_set.copy()
print(new_set)
my_set.pop()
print(my_set)
