# List slicing is a property in which the list can have different steps and itterations which can be customised.
# Example of List Slicing

amazon_cart = ['Pineapple','Potato','WaterMelon','MonsterDrink','Biscuits']

print(amazon_cart[0::2]) #The list will follow the itteration from starting to end with skipping one index.

#The above code will print Pineapple, Watermelon and Biscuits. As the step index was 2.
#Lists are mutable, whereas strings aren't. Because of this property lists will be used extensively.

amazon_cart[2] = "Orange" #This is replacing watermelon with orange to show the mutable property of Lists. 
new_cart = amazon_cart[0:2] #Copying the amazon_cart elements till 2nd index to new_cart.
new_cart[1] = 'waffles'

#If we copy the entire items of amazon_cart to new_cart. What would happen? 
new_cart = amazon_cart[:] #Both the outputs of the cart will have exact same items. This happens because new_cart is assigned to amazon_cart and the values of amazon_cart changes in the memory device.
new_cart[0] = "Desktop"
print(new_cart)
print(amazon_cart)
new_cart = amazon_cart[:] #This will make sure to copy all the elements of amazon_cart to new_cart without changing the amazon_cart value. 
print(amazon_cart)
print(new_cart)
