def solution(box, n):
    result = 1
    for i in range(len(box)):
        result *= (box[i] // n)

    return result

print(solution([10, 8, 6], 3))