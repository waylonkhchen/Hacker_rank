def jumpingOnClouds(c):
    path = [0]
    i = 0
    while i < len(c) - 2:
        if c[i + 2] == 0:
            path += [i + 2]  
            i += 2
        else:
            path += [i + 1]
            i += 1
        print(path)
    if path[-1] != len(c) - 1:
        path += [len(c) - 1]
    result = len(path) - 1

    return result


print('results is', jumpingOnClouds([0, 0, 1, 0, 0, 0, 1, 0]))
