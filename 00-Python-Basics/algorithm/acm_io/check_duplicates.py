
n = int(input())
numbers = list(map(int, input().split()))

seen = set()
has_duplicate = False

for number in numbers:
    if number in seen:
        has_duplicate = True
        break

    seen.add(number)

if has_duplicate:
    print("YES")
else:
    print("NO")


