finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


# 정렬이 되지 않은 배열에서는 이진탐색이 불가능
# 즉, 항상 일정한 규칙으로 정렬이 되어있어야 이진탐색이 가능함
# 이 문제는 낚시문제
def is_exist_target_number_binary(target, numbers):
    # min = 0
    # max = len(numbers) - 1
    # while(min <= max):
    #     center = (min + max) // 2
    #     if numbers[center] == target:
    #         return True
    #     elif numbers[center] > target:
    #         max = numbers[center]
    #     elif numbers[center] < target:
    #         min = numbers[center]
    #     return False

    return 1




result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)