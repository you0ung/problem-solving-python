def solution(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        if factorial > n:
            return i - 1
        
print(solution(3628800))