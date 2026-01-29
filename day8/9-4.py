def solution(balls, share):
    result = 1
    for i in range(share):
        result *= balls
        balls -= 1
    for i in range(share):
        result //= i + 1
        share -= 1

    return result
        
print(solution(3, 2))