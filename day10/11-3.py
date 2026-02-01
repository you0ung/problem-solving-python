def solution(numbers):
    order = sorted(numbers, reverse=True)
    result = order[0] * order[1]
    
    return result

print(solution([1, 2, 3, 4, 5]))