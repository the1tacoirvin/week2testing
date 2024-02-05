def main1():
    '''to solve the first matrix, this is put under an entire main1 function'''
    def seidel(a, x, b):
        '''this is to get the seidel function, like the one to solve it and fix the zero values. i think that's what we're finding?'''
        # Finding length of a(3)
        n = len(a)
        # for loop for 3 times as to calculate x, y , z
        for j in range(0, n):
            # temp variable d to store b[j]
            d = b[j]

            # to calculate respective xi, yi, zi
            for i in range(0, n):
                if (j != i):
                    d -= a[j][i] * x[i]
            # updating the value of our solution
            x[j] = d / a[j][j]
        # returning our updated solution
        return x


    # int(input())input as number of variable to be solved
    n = 3
    a = []
    b = []
    # initial solution depending on n(here n=3)
    x = [0, 0, 0]
    a = [[3, 1, -1], [1, 4, 1], [2, 1, 2]]
    b = [2, 12, 10]
    print(x)

    # loop run for m times depending on m the error value
    for i in range(0, 25):
        x = seidel(a, x, b)
        # print each time the updated solution
        print(x)
def main2():
    '''to solve the second matrix, this is put under an entire main2 function'''
    def seidel(a, x, b):
        '''this is to get the seidel function, like the one to solve it and fix the zero values. i think that's what we're finding?'''
        # Finding length of a(3)
        n = len(a)
        # for loop for 3 times as to calculate x, y , z
        for j in range(0, n):
            # temp variable d to store b[j]
            d = b[j]

            # to calculate respective xi, yi, zi
            for i in range(0, n):
                if (j != i):
                    d -= a[j][i] * x[i]
            # updating the value of our solution
            x[j] = d / a[j][j]
        # returning our updated solution
        return x


    # int(input())input as number of variable to be solved
    n = 3
    a = []
    b = []
    # initial solution depending on n(here n=3)
    x = [0, 0, 0, 0]
    a = [[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4]]
    b = [-1, 2, 7, 3]
    print(x)

    # loop run for m times depending on m the error value
    for i in range(0, 25):
        x = seidel(a, x, b)
        # print each time the updated solution
        print(x)
if __name__ == "__main__":
    '''this just prints the values'''
    main1()
    print("gap")
    main2()