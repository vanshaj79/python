def print_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="shaktiman", age="22")
# print_kwargs(name="shaktiman", age="22")
