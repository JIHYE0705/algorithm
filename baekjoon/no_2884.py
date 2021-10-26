# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
# 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다.
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
# 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.


num = input().split()

hour = int(num[0])
minute = int(num[1]) - 45

if minute < 0:
    minute += 60
    hour -= 1

    if hour <= 0:
        hour += 24

if hour == 24:
    hour = 0

print(hour, minute)


