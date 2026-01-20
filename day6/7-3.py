def solution(n, k):
    sheep = 12000
    drink = 2000

    service = n // 10

    result = sheep * n + drink * (k - service)

    return result

print(solution(64, 6))