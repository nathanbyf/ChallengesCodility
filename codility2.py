def solution(N):
    br = str(bin(N))[2:]
    print(type(br), br)
    br_group = False
    br_highest = 0
    bin_zero_counter = 0
    for char in br:
        print("CHAR", char)
        if char == "1":
            print("POINT 1", br_highest, bin_zero_counter)
            if br_highest < bin_zero_counter:
                br_highest = bin_zero_counter
            br_group = True
            bin_zero_counter = 0
        elif br_group:
            bin_zero_counter += 1
            print("POINT 2", br_highest, bin_zero_counter)
    return br_highest


x = solution(2222)

print(x)
