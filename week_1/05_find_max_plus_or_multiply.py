input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for i in range(len(array)):
        if answer == 0 or array[i] == 1:
            answer += array[i]
        else:
            answer *= array[i]
    return answer

    # 선생님 답

    # multiply_sum = 0
    # for number in array:
    #     if number <= 1 or multiply_sum <= 1:
    #         multiply_sum += number
    #     else:
    #         multiply_sum *= number
    # return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)
