# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
from math import ceil

X = 10
Y = 85
D = 30


def solution(X, Y, D):
    distance = Y - X

    number_of_jumps = distance / D

    jumps = ceil(number_of_jumps)

    return jumps


print(solution(X, Y, D))
