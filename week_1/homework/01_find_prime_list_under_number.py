input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!

    # 소수를 구하는 코드 짜기
    # └> 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
    # └> 주어진 자연수 N이 소수이기 위한 필요충분 조건은
    #     └> N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
    #     └> 수가 수를 나누면 몫이 발생하는데, 몫과 나느는 수 둘 중 하나는 반드시 N의 제곱근 이하이다.

    prime_list = []

    for n in range(2, number + 1):  # n <- 2 ~ number
        for i in prime_list:  # i <- 2 ~ n - 1 n - 1 이하의 소수로 나누어지는지 확인인
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
