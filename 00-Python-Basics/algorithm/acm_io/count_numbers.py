
n = int(input())
number_list = list(map(int,input().split()))
count_positive = 0
count_negative = 0
count_zero = 0

for number in number_list:
    if number > 0:
        count_positive += 1
    if number < 0:
        count_negative += 1
    if number == 0:
        count_zero += 1
        
print(count_positive)
print(count_negative)
print(count_zero)
