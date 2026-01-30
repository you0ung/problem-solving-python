def solution(numbers, k):
    idx = (k - 1) * 2 % len(numbers)
    result = numbers[idx]
    return result

print(solution([1, 2, 3, 4, 5, 6], 5))