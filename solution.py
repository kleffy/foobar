def solution(area):
    """
    Write a function solution(area) that takes as its input a single unit of measure representing 
    the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list 
    of the areas of the largest squares you could make out of those panels, starting with the 
    largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].
    """
    result = []
    while area > 0:
        side = int(area ** 0.5)
        largest_square = side ** 2
        result.append(largest_square)
        area -= largest_square
    return result



print(solution(15324))
