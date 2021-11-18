case = int(input())

for i in range(case):
    score_list = list(map(int, input().split(' ')))

    student = score_list.pop(0)
    total = sum(score_list)
    avg = total / student

    count = 0
    for score in score_list:
        if score > avg:
            count += 1
    percent = (count / student) * 100

    print(f'{percent:.3f}%')


