def solution(age):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    result = ""

    for ch in str(age):
        result += char[int(ch)]

    return result

print(solution(51))