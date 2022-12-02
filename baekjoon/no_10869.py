# 두 자연수 A와 B가 주어진다.
# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

number = input().split()

num1 = int(number[0])
num2 = int(number[1])

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(int(num1 / num2))
print(num1 % num2)
