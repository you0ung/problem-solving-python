def not_prime(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count 

def solution(n):
    result = []
    for i in range(1, n+1):
        if not_prime(i) >= 3:
            result.append(i)

    return len(result)

print(solution(15))