basket = [1,2,3,4,5]
print(len(basket))
print(type(basket))
# adding
basket.append(6)
new_basket = basket
print(basket)
print(new_basket)
# insert 
basket.insert(3, 69)
print(basket)
# extend 
new_list = basket.extend([100])
print(basket)
#removing

basket.pop()
basket.pop(0)
print(basket)
basket.remove(69)
print(basket)

basket.clear()
print(basket)


