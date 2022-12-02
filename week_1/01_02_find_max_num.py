input = [3, 5, 6, 1, 2, 4]


# 선생님 답 1
# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break;
#         else:
#             return num


# 선생님 답 2
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result = find_max_num(input)
print(result)
