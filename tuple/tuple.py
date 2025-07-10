tea_types = ("black", "green", "oolong")
print(tea_types)

print(tea_types[0])
print(tea_types[-2]) # green 

# if we exceed the limit by -4, -5 ....etc. it gives an error of index out of range 

# can not change the value means immutable
# tea_types[0] = "lemon"

more_types = ("earl grey", "herbal")

# will get a new tuple
all_tea = tea_types + more_types
print(all_tea)

# gives you the count of value in the tuple
print(more_types.count("herbal"))