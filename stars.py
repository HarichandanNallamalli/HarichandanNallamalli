N = int(input())
print("* " * (2 * N))
in_spaces_count = 0
for i in range(1 , N):
    in_spaces_count = in_spaces_count + 4
    in_spaces = " " * in_spaces_count
    pattern = ("* " * (N - i)) + in_spaces + ("* " * (N - i))
    print(pattern)

in_spaces_count = in_spaces_count + 4
for i in range(1 , N):
    in_spaces_count = in_spaces_count - 4
    in_spaces = " " * in_spaces_count
    pattern = ("* " * i) + in_spaces + ("* " * i)
    print(pattern)
