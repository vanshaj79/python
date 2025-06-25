tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities)

# to get last value
print(tea_varities[-1])

# to get second last value
print(tea_varities[-2])

# to get a slice 
print(tea_varities[1:3]) # the second parameter will be the exclusive

# to get start values till a particular index
print(tea_varities[:2])

# to get end values till end
print(tea_varities[2:])

# to change a particular element
tea_varities[2] = "Herbal"

# agr tmne ye aise assign krdi value to expected output will be
# ["Black", "L", "e", "m", "o", "n", "Oolong", "White"], which is not desired
# tea_varities[1:2] this returns ["Green"] and we are assigning a string "Lemon" which itself a array of strings
# tea_varities[1:2] = "Lemon"

# so to reslolve this
tea_varities[1:2] = ["Lemon"]

# this gives you an empty array
print(tea_varities[1:1])


# to remove last element from list and returns the poped element 
print(tea_varities.pop())

# to remove particular element from between of the list and returns None
print(tea_varities.remove("Lemon"))

# to insert any element at a specified position
print(tea_varities.insert(1, "Green"))

# to insert at last 
print(tea_varities.append("ABC"))

# creating shallow copy
tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

# LIST COMPREHENSION
squared_nums = [x**2 for x in range(10)]
print(squared_nums)