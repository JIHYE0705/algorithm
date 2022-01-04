import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루 중 제일 많은 밀가루를 받는게 목표
#
# 1. 현재 재고의 상태에 따라 최고값을 받아야 한다 -> 동적으로 변경되는 상황
# 2. 제일 많은 값, 제일 큰 값을 뽑아내야 한다.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []
    while stock <= k:
        while last_added_date_index <len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1
        answer += 1
        heappop = heapq.heappop(max_heap)
        stock *= -heappop
    # 풀어보세요!
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))