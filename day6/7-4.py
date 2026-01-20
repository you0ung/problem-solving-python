def solution(n):
    even = 0
    for i in range(n+1):
        if i % 2 == 0:
            even += i

    return even

print(solution(10))