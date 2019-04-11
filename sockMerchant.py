def sockMerchant(n, ar):
    unique = []
    mydict = {}
    for i in ar:

        if i not in unique:
            unique = unique + [i]

            mydict[i] = 1
        else:
            mydict[i] += 1
    results = list(mydict.values())
    result = [i // 2 for i in results]
    result = sum(result)
    return result


print(sockMerchant(10, [1, 2, 1, 2, 1, 1, 3, 2, 3, 4]))
