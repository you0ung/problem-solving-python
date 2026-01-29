def solution(emergency):
    result = []
    order = sorted(emergency, reverse=True) # 내림차순
    # order = [76, 24, 3]
    # emergency = [3, 76, 24]

    for i in range(len(emergency)):
        result.append(order.index(emergency[i])+1)

    return result

print(solution([3, 76, 24]))