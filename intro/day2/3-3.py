def solution(array):
    array.sort()

    num = array[0]
    max_count= count = 1

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            count += 1
        else:
            count = 1

        if max_count < count:
            max_count = count
            num = array[i]
        elif max_count == count:
            num = -1

    return num

print(solution([1, 1, 2, 2]))