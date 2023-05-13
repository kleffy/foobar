def solution(n):
    n = long(n)
    step = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        step += 1
    return step



print(solution('4'))  # Output: 2
print(solution('15'))  # Output: 5
