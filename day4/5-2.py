def solution(money):
    coffee = 5500
    result = []

    count = money // coffee
    change = money % coffee

    result.extend([count, change])

    return result

print(solution(15000))