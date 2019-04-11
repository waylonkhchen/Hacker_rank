def minimumBribes(q):
    default = range(1, len(q) + 1)
    checker = [qq - dd for qq, dd in zip(q, default)]
    counter = 0
    if any([i > 2 for i in checker]):  # return chaotic when more than 2 bribes are done by one person
        return 'Too chaotic'
    else:
        for i in range(1, len(q)):
            for j in range(i):
                if q[j] > q[i]:
                    counter += 1

    # if checker.any() >
    return counter


print(minimumBribes([2, 1, 5, 3, 4]))
# print(any(test >= 2)
