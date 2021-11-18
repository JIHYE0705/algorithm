num = set(range(1, 10001))
remove = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    remove.add(i)
num = num - remove
for k in sorted(num):
    print(k)