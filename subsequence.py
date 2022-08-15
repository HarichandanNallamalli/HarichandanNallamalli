first_string = input()
second_string = input()
second_index = 0
second_length = len(second_string)
for char in first_string:
    if char == second_string[second_index]:
        second_index += 1
        if second_index == second_length:
            break
if second_index == second_length:
    print("Yes")
else:
    print("No")
