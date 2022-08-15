def fibonacci(n):
    if n <= 1: # Complete this function
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input())
result = fibonacci(n)# call the fibonacci function
print(result)
