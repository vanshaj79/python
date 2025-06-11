input_Str = "teeteracdacd"

for char in input_Str:
    if input_Str.count(char) == 1: # count() function counts the number of occurence of the particular char in the string 
        print("char is",char)
        break