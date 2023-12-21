# https://app.codility.com/demo/results/trainingBP48DP-UBA/


def solution(A):
    length = len(A)

    if length + 1 not in A:
        return length + 1
    elif 0 not in A:
        return 0

    for i in sorted(A):
        if i + 1 not in A and i != A[-1]:
            return i + 1
        # if i -1 not in A and i != A[0]:
        #    return i + 1
        if i - 1 not in A and i >= 1:
            return i - 1
        else:
            return 0


print(solution(A))
