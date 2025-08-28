# time complexity - O(n2)


def longest_unique_substring(s):
    current = ""    # abhi tak ka dabba (substring)
    longest = ""    # sabse bada dabba (answer)

    for ch in s:   # ek-ek letter uthao
        if ch in current:
            # repeat mila -> dabba kaat do repeat ke baad se
            pos = current.index(ch)   # repeat kahan mila
            current = current[pos+1:] + ch
        else:
            # repeat nahi -> normal add karo
            current = current + ch

        # longest update karo
        if len(current) > len(longest):
            longest = current

    return longest

print(longest_unique_substring("bacab"))

