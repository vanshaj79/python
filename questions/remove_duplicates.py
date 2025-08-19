nums = [1,2,3,2,4,1,5]

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)
        
print(unique)