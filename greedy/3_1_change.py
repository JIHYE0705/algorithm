change = int(input())
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += change // coin
    change %= coin

print(count)
