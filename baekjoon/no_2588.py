num1 = int(input())
num2 = int(input())

multiply = num1 * num2

while num2 / 10 > 0:
    multiply_number = num2 % 10
    print(num1 * multiply_number)
    num2 = int(num2 / 10)

print(multiply)
