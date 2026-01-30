def solution(numbers, direction):
    result = []
    if direction == "right":
        result.append(numbers[-1])
        for i in range(len(numbers)-1):
            result.append(numbers[i])
    elif direction == "left":
        for i in range(0, len(numbers)-1):
            result.append(numbers[i+1])
            # result = [455, 6, 4, -1, 45, 6]
        result.append(numbers[0])

    return result

print(solution([4, 455, 6, 4, -1, 45, 6], "left"))