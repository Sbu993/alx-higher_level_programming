#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in row:
            if a is not row[len(row) - 1]:
                print("{:d}".format(a), end=" ")
            else:
                print("{:d}".format(a), end="")
        print()

# for row in matrix:
#     print(" ".join("{:d}".format(a) for a in row))
