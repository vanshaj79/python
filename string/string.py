chai = "Masala Chai"

first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

slice_chai1 = chai[-6:-1]
print(slice_chai1) # output: a cha

num_list = "0123456789"
print(num_list[:]) # gives you the full string
print(num_list[3:]) # gives - 3456789
print(num_list[:7]) # gives - 0123456
print(num_list[0:7:2]) # gives - 0246, actually it hops the string by thevalue whatever we give in the third argument

print(chai.lower()) # converts the string into small letters
print(chai.strip()) # removes extra spaces from the string 

print(chai.replace("Masala", "Lemon")) # replaces the string chars with other char
print(chai.split()) # splits the string into array of elements
print(chai.find("Chai")) # returns the positon of the string if finds otherwise returns -1.


# fromatting the string 

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))