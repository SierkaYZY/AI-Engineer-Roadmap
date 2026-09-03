
n = int(input())
numbers = list(map(int,input().split()))
target = int(input())

left = 0
right = len(numbers)-1

while left <= right :
    mid = (left+right)// 2
    if numbers[mid] == target:
        print(mid)
        break
    elif numbers[mid] < target:
        left = mid+1
    else:
        right = mid-1

if left > right:
    print(-1)