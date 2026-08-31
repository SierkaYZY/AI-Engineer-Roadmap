
numbers = list(map(int,input().split()))
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

max_number = None
max_count = 0
for number,count in counts.items():
    if count > max_count:
        max_count = count
        max_number = number

print(max_number)

