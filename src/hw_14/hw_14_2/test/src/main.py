from matrix_classes import Matrix
from random import randint as rd
from matrix_funcs import (
    max_matrix,
    min_matrix,
    summ_matrix,
)


def main():
    matrix_1 = Matrix([[rd(0, 9) for x in range(10)] for y in range(10)])
    print(matrix_1,
          max_matrix(matrix_1),
          min_matrix(matrix_1),
          summ_matrix(matrix_1))


if __name__ == '__main__':
    main()
