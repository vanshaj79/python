def sum_of_all(*args):
    # print(*args)
    print(args)
    # for i in args:
    #     print(i)
    return sum(args)

print(sum_of_all(1,2))
print(sum_of_all(1,2,3))
print(sum_of_all(1,2,3,4))
print(sum_of_all(1,2,3,4,5))
    