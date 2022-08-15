def get_con_sum_list(int_list):
    con_sum_list = []
    for i in range(len(int_list)-1):
        sum = int_list[i] + int_list[i+1]
        con_sum_list.append(sum)
    return con_sum_list

def triangle(int_list):
    while len(int_list) > 1:
        con_sum_list = get_con_sum_list(int_list)
        print(con_sum_list)
        int_list = con_sum_list

def con_list_to_int(args):
    int_list = []
    for i in args:
        num = int(i)
        int_list.append(num)
    return int_list

N = input().split(",")
int_list = con_list_to_int(N)
print(int_list)
triangle(int_list)
