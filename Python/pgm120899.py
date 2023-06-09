def solution(array):
    answer = []
    temp = [i for i in array]
    answer = [max(temp), temp.index(max(temp))]

    return answer
