input = "hello world"


def count_vowels(input):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in input:
        if ch in vowels:
            count += 1

    return count


print(count_vowels(input))
