

def solution():
    matrix = [[1, 2, 3], [4,5,6],[7,8,9]]

    cache = [0,0,0,0,0]

    for i in range(0, 3):
        for j in range(0, 3):
            print(i, j)
            if j==0:

                cache[3-i -1] += matrix[i][j]
            else:
                cache[3 - i + j - 1] += matrix[i][j]
    print(cache)
if __name__ == "__main__":
    s_2 = solution()