def solution(array):
    answer = []
    temp = [i for i in array]
    answer = [max(temp), temp.index(max(temp))]
    return answer


array = [9, 10, 11, 8]
print(solution(array))
solution(array)
