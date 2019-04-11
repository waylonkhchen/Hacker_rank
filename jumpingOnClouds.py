def jumpingOnClouds(c):
    paths = [[0]]
    for i in range(len(c) - 2):
        for j, path in enumerate(paths):
            if path[-1] == i:
                print(paths)
                if c[i + 1] == 0 and c[i + 2] == 0:
                    paths += [path + [i + 1]]  # bifurcation, one is path +[c[i+1]]
                    paths[j] += [i + 2]  # the other is  path +[c[i+2]]
                if c[i + 1] == 0 and c[i + 2] == 1:
                    paths[j] += [i + 1]
                if c[i + 1] == 1 and c[i + 2] == 0:
                    paths[j] += [i + 2]
    paths = [(path + [len(c) - 1]) if path[-1] != len(c) - 1
             else path for path in paths]
    result = min([len(x) for x in paths]) - 1
    return result
