def solution(price):
    if price >= 500000:
        pay = price * 0.8
    elif price >= 300000:
        pay = price * 0.9
    elif price >= 100000:
        pay = price * 0.95
    else:
        pay = price
        
    return int(pay)

print(solution(150000))