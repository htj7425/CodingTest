def solution(numbers, direction):
    first = [numbers[0]]
    middle = numbers[1 : len(numbers) - 1]
    last = [numbers[len(numbers) - 1]]
    answer = []
    if direction == "right":
        answer.extend(last)
        answer.extend(first)
        answer.extend(middle)
    else:
        answer.extend(middle)
        answer.extend(last)
        answer.extend(first)
    return answer
