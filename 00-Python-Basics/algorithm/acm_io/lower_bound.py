
n = int(input())
numbers = list(map(int,input().split()))
target = int(input())

left = 0
right = n-1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] >= target:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)