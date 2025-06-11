distance = 3

if distance < 3:
    mode = "walk"
elif distance <= 15:
    mode = "bike"
else:
    mode = "car"
    
print("your distance is",distance,"you should go with",mode)