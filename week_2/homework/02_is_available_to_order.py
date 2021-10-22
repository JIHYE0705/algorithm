shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]




def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!

    # O((N + M) * logN)
    # shop_menus.sort()  # 정렬의 시간 복잡도는 배열의 길이(= N)
    # # O(N * logN)
    # for order in orders:  # O(M * logN)
    #     if not is_existing_target_number_binary(order, shop_menus):  # 이분탐색의 시간복잡도 : O(logN)
    #         return False
    #
    # return True

    # 중복없는 집합자료형 set 사용
    # O(N) + O(M) = O(N+M)
    menus_set = set(menus)      # O(N)
    for order in orders:        # M
        if order not in menus_set:  # O(1)
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    while (current_min <= current_max):
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
