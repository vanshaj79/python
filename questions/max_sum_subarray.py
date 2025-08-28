input = [1, 10, 3, 4, 5, 6]

def max_sum_subarray(arr, k):
    start = 0
    size = len(arr)
    end = 0
    window_sum = 0
    max_sum = 0

    while end < size:
        window_sum += arr[end]

        if end - start + 1 == k:
            # window full ho gayi → max update + slide
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1

        end += 1   # <- har round me end ko aage badhana zaroori hai

    return max_sum

print(max_sum_subarray(input, 3))  # Output: 15 (4+5+6)
