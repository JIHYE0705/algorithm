numbers = [2, 3, 1]

target_number = 0

# 1) +2 +3 +1 = 6           +++
# 2) +2 +3 -1 = 4           ++_
# 3) +2 -3 +1 = 0   타겟!    +_+
# 4) +2 -3 -1 = -2          +__
# 5) -2 +3 +1 = 2
# 6) -2 +3 -1 = 0   타겟!
# 7) -2 -3 +1 = -4
# 8) -2 -3 -1 = -6

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의수를 추가

result_count = 0
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):

    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index])

    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index])




print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number,0, 0))  # 5를 반환해야 합니다!

print(result_count)