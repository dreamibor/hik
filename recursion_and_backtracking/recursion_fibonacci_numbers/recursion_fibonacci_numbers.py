def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # Write your code here.

n = int(input())
print(fibonacci(n))