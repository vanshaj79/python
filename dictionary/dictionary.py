chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types)

# to access with keys
print(chai_types["Ginger"])

# to change the value of the key
chai_types["Green"] = "Fresh"

# to loop over the dictionary
for chai in chai_types:
    print(chai, chai_types[chai])
    
# another way
for key, value in chai_types.items():
    print(key, value)
    
# checking a particular key in dictionary
if "Masala" in chai_types:
    print("I have masala chai")
    
# adding new key in dictionary
chai_types["Earl Grey"] = "Citrus"

print(chai_types)
 
# to remove the key from dictionary
chai_types.pop("Ginger")

print(chai_types)

del chai_types["Earl Grey"]

# creating shallow copy
chai_types_copy = chai_types.copy()


# creating nested dictionary
tea_shop = {
    "chai": {"masala": "spicy", "ginger": "zesty"},
    "tea": {"green": "mild", "black": "strong"}
}

print(tea_shop)
# calling a subset
print(tea_shop["chai"])

print(tea_shop["chai"]["masala"])