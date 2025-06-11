age = 25

def categorize_age(age):
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 50:
        print("Adult")
    else:
        print("Senior")

categorize_age(age)