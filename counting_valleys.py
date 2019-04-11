def countingValleys(n, s):
    current = 0
    valleys = 0
    for i in s:
        print(current)
        if i == 'D':
            if current == 0:
                valleys += 1
            current -= 1
        else:
            current += 1
    return valleys


print('valleys=', countingValleys(8, 'UDDDUDUU'))
