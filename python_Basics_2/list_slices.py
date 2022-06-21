# string slices just for fun 
string = 'Hello Frey'
print(string[0:4:1])
# Hell lol 
flipkart_cart = [
	'Hand gripper',
	'Sunglasses',
	'Strangers Things CD',
	'G-Link KeyBoard',
	'48 Laws Of Power'
	]

# check your whole cart 
print(flipkart_cart)

# only want to check out for  Hand gripper and Sunglasses 

print(flipkart_cart[0:2])

# let's skip every second one 

print(flipkart_cart[0::2])

# ohh why should i buy keyboard when i can buy whole laptop 
# let's change it 

flipkart_cart[3] = 'Laptop' # Now it's added in out cart 
print(flipkart_cart)	

# now i don't like  this whole fucking list name and items 
# so as a good hacker we will change everything 

flipkart_cart = ['Hack the box T-shirt', 'rubber duckey']

frey_list = flipkart_cart

print(frey_list)

print(flipkart_cart) #now we have also cracked that previous list HAHAHAHAHA............

# tip but as a ethical hacker we don't do that we just copy out the list with using ---> [:]


