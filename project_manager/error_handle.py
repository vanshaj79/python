file = open('youtube.txt', 'w')


# to write a file i have these two ways

# first way
try:
    file.write('chai or code')
finally:
    file.close()

# second way 
with open('youtube.txt', 'w') as file:
    file.write('chia seeds')