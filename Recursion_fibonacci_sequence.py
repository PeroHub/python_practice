#The first few terms of the fibonacci sequence are 1,1,2,3,5,8,13,21

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,11):
    print(n, ":", fibonacci(n))