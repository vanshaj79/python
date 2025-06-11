import math

def decimal_formatter(num):
    formatted = "{:.2f}".format(num)
    return formatted


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return decimal_formatter(area), decimal_formatter(circumference)


a ,c = circle_stats(4)

print("Area:",a,"Circumference:",c)
