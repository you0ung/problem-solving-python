def solution(num_list):
    result = []
    even = 0
    odd = 0

    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    result.extend([even, odd])

    return result

print(solution([1, 2, 3, 4, 5]))