# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

import pandas as pd

A = [3, 8, 9, 7, 6]


def solution(A, K):
    A = pd.Series(A)

    K = K % len(A)
    return A[-K:] + A[:-K]


A = [9, 3, 9, 3, 9, 7, 9]


def solution(A):
    result = pd.Series(A).value_counts()

    for i, v in zip(result.index, result.values):
        if v <= 1:
            odd = i

    return odd


print(solution(A))
