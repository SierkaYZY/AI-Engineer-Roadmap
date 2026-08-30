
n = int(input())
numbers = input()
number_list = list(map(int, numbers.split()))

sums = 0

for i in range(n):
    sums += number_list[i]

print(sums)

