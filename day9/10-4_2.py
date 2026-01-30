# 인덱스 이용
def solution(numbers, direction):
    result = 0
    if direction == "right":
        result = numbers[-1:] + numbers[:-1]
    else: # "left"
        result = numbers[1:] + numbers[:1]
        
    return result

print(solution([1, 2, 3], "right"))