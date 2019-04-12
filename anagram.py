def anagram(s1, s2):

    def histogram(astring):
        adict = {}
        for e in astring:
            # print(e)
            if e not in adict:
                adict[str(e)] = 1
            else:
                adict[str(e)] += 1
        return adict

    if len(s1) != len(s2):
        return -1
    hist1 = histogram(s1)
    hist2 = histogram(s2)
    print(hist1)
    print(hist2)
    # newdict is the difference of a and b
    newdict = {}
    for e1 in s1:
        try:
            newdict[e1] = hist1[e1] - hist2[e1]
        except KeyError:
            newdict[e1] = hist1[e1]
    result = sum([val if val > 0 else 0 for val in newdict.values()])
    return result


print(anagram('mn', 'op'))
