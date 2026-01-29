def solution(hp):
    count = hp // 5
    count += (hp % 5) // 3
    count += (hp % 5) % 3

    return count

print(solution(3))