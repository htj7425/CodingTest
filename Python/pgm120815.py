def solution(n):
    answer = 1
    for i in range(100):
        if answer * 6 % n == 0:
            break
        else:
            answer += 1
    return answer
