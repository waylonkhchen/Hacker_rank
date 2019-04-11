def minimumSwaps(arr):
    def swap(alist, e1, e2):
        i1, i2 = alist.index(e1), alist.index(e2)
        alist[i2], alist[i1] = alist[i1], alist[i2]

    swap_count = 0
    skip_index = []
    for i, a in enumerate(arr):
        if i in skip_index:
            continue  # skip checking if it's already swapped
        else:
            if i + 1 != a:
                swap(arr, arr[i], i + 1)  # swap to make arr[i] == i+1,
                swap_count += 1
                if arr.index(a) + 1 == a:
                    skip_index += [a - 1]  # if a is in position after swap, skip it for swap later in the loop
    return swap_count


arr = [4, 3, 1, 2]
print(minimumSwaps(arr))

# arr_hash = dict(list(enumerate(arr)))
