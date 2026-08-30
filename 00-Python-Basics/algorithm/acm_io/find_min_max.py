
n = int(input())
numbers = input()
number_list = list(map(int, numbers.split()))
max_number = number_list[0]
min_number = number_list[0]
for number in number_list:
    if number > max_number:
        max_number= number
    if number < min_number:
        min_number = number

print(max_number)
print(min_number)
