from collections import deque

c = 11
b = 2


# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1 만큼 움직임
# 즉 증가하는 속도가 1초마다 1씩 증가

# 브라운의 위치 변화
# B - 1, B + 1 , 2 * B

# 모든 경우의 수를 다 나열
# BFS 사용

# 잡았다! 라는 의미는 똑같은 시간에 똑같은 위치에 존재해야 합니다
# 시간은 1씩 증가
# 코니,브라운 위치는 값이 자유자재로 변함

# 규칙적 -> 배열, 자유자재 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치 저장
# [{ }]


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 담아줄게요!.
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):  # Q. Queue 인데 while 을 안 쓰는 이유를 고민해보세요!
            current_position, current_time = queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
