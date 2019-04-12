def hourglassSum(arr):

    def glassSum(arr2d, i, j):
        glass = arr2d[i][j:j + 3] + [arr2d[i + 1][j + 1]] + arr2d[i + 2][j:j + 3]
        return sum(glass)
    glassSum_list = [glassSum(arr, i, j) for i in range(4) for j in range(4)]
    return max(glassSum_list)

    # def glassSum(arr2d, i, j):
    #     glass = arr2d[i][j:j + 3] + [arr2d[i + 1][j + 1]] + arr2d[i + 2][j:j + 3]
    #     return sum(glass)

    # arr2d = [[5, 0, 1], [0, 1, 0], [0, -1, -1]]
    # i = 0
    # j = 0
    # print(arr2d[i][j:j + 3] + [arr2d[i + 1][j + 1]])
    # print(glassSum(arr2d, 0, 0))
