list_a = input().split(",")
list_b = input().split(",")
first_list = []
for i in list_a:
    num = int(i)
    first_list.append(num)
second_list = []
for i in list_b:
    num = int(i)
    second_list.append(num)
set_a = set(first_list)
set_b = set(second_list)

result_set = set_a.intersection(set_b)
result_list = list(result_set)
result_list.sort()
print(result_list)
