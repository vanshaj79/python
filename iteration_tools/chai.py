import time

print("chai is here")

username = "hitesh"

print(username)


# >>> f = open('chai.py')
# >>> f.readline()
# 'import time\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'print("chai is here")\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'username = "hitesh"\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> for line in open('chai.py')
#   File "<stdin>", line 1
#     for line in open('chai.py')
#                                ^
# SyntaxError: expected ':'
# >>> for line in open('chai.py').readlines()
#   File "<stdin>", line 1
#     for line in open('chai.py').readlines()
#                                            ^
# SyntaxError: expected ':'
# >>> for line in open('chai.py').readlines():
# ... print(line)
#   File "<stdin>", line 2
#     print(line)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for line in open('chai.py').readlines():
# ...     print(line)
# ... 
# import time



# print("chai is here")



# username = "hitesh"



# print(username)

# >>> myList = [1,2,3,4]
# >>> I = iter(myList)
# >>> I
# <list_iterator object at 0x77d710ecefe0>
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I
# <list_iterator object at 0x77d710ecefe0>
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> f = open('chai.py')
# >>> iter(f)
# <_io.TextIOWrapper name='chai.py' mode='r' encoding='UTF-8'>
# >>> iter(f) is f
# True
# >>> 