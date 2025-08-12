input = 5
output = None


def findfact(num):
    if num <= 1:
        return 1
    return num * findfact(num - 1)


print(findfact(input))
