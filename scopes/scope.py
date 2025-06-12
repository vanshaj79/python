username = "chaiorcode"


def func():
    username = "chai"
    print(username)

func()
print(username)

x = 90

def func1():
    global x # this is representing the global x variable
    x = 10

func1()
print(x)

i = 100
def outer():
    i = 10 # if it doesn't find in the parent function scope then it will go to global scope
    def inside():
        print(i)
    return inside

result = outer()
result()

def power(num):
    def number(of):
        return of ** num
    return number

g = power(2)
print(g(4))