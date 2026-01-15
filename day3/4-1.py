def solution(n):
    if n <= 7:
        pizza = 1
    else:
        pizza = n // 7
        if n % 7 > 0:
            pizza += 1

    return pizza

print(solution(15))