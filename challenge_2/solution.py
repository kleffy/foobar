def solution(s):
    salutes = 0
    employees_going_right = 0

    for char in s:
        if char == '>':
            employees_going_right += 1
        elif char == '<':
            salutes += 2 * employees_going_right

    return salutes
