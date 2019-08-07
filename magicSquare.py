
def generateMagicSquare(n):
    mSquare = [[0 for _ in range(n)] for _ in range(n)]

    i , j = 0, n // 2
    num = 1

    while num <= pow(n, 2):
        mSquare[i, j] = num
        num += 1
        ni, nj = (i - 1) % n , (j + 1) % n
        if(mSquare[ni, nj]):
            i += 1
        else:
            i, j = ni, nj

    return mSquare






if __name__ == "__main__":
    inp = int(input())

    magicSquare = generateMagicSquare(inp)

    print(magicSquare)