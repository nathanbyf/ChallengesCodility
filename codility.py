def solution(number):
    """Solution method implementation."""
    # initialize result variable. This will hold the max gap.
    result = 0
    # initialize a boolean to mark if the start of the gap
    started = False
    # initialize a current gap variable
    gap = 0
    # create a copy of the number argument to work on
    num = number
    # while loop processing
    while num > 0:
        print("NUM", num)
        # if the bit is 1, we just started a new gap
        if num % 2:
            gap = 0
            started = True
        # else, if the bit is 0 and a gap is started,
        # increment current gap and update the maximum gap
        elif started:
            gap += 1
            result = max(result, gap)
        # integer-divide the number by 2
        num //= 2
        print("GAP", gap)
    # return the maximum gap found after the processing
    return result


S = "011100"


def solution2(S):
    operations = 0

    number = int(S, 2)

    while number > 0:
        print(number)
        if number % 2 == 0:
            number = number / 2
            operations += 1
        else:
            number = number - 1
            operations += 1

    return operations


print(solution2(S))

s2 = "111"

print(solution2(s2))
