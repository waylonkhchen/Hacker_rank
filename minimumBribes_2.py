def minimumBribes(q):
    default = range(1, len(q) + 1)
    checker = [qq - dd for qq, dd in zip(q, default)]
    counter = 0
    subcounter = 0
    if q[0] - 1 > 2:
        return 'Too chaotic'
    for i in range(1, len(q)):
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'  # precheck
        for j in range(i):
            if q[j] > q[i]:
                counter += 1
        if (max(q[:i]) < q[i]) and (sorted(q[i:]) == q[i:]):
            break
    return counter


print(minimumBribes([2, 1, 5, 3, 4]))


# print([i for i in range(0)])
