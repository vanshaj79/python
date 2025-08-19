nested = [1, [2, 3], [4, [5, 6]], 7]


def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))  # agar list hai → recursion
        else:
            flat.append(item)
    return flat


print(flatten(nested))
