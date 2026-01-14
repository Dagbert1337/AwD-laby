


def main():

    y = [[0]*3]*3
    y[1][1]=11
    print(type(y))
    print(type(y[0]))
    print(y)

    
    z = [[col for col in range(3)] for _ in range(3)]
    z[1][1] = 11
    print(type(z))
    print(type(z[0]))
    print(z)

    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x[1][1] = 11
    print(type(x))
    print(type(x[0]))
    print(x)

    n=3
    golden = [[0] * n for _ in range(n)]
    golden[1][1]=11
    print(golden)





if __name__ == "__main__":
    main()