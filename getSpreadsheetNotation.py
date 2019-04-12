def getSpreadsheetNotation(n):
    # Write your code here
    r = (n - 1) // (702) + 1
    cc = n % 702

    c1 = (cc) // 26
    c2 = (cc) % 26
    c1_A2Z = [''] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    c2_A2Z = ['Z'] + [chr(i) for i in range(ord('A'), ord('Z'))]

    c1dict = dict(list(enumerate(c1_A2Z)))
    c2dict = dict(list(enumerate(c2_A2Z)))

    result = str(r) + str(c1dict[c1]) + str(c2dict[c2])

    print('r=', r, 'c1=', c1, 'c2=', c2)
    return result
