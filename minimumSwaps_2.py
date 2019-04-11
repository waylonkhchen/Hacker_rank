def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] == i + 1:
            i += 1
            continue
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]  # this is how python swap
        swaps += 1
    return swaps
