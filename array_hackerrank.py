#Given an array,A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
n = int(input())

arr = list(map(int, input().rstrip().split()))

reserved_array = []
for i in range(n):
    reserved_array.append(arr[n-i-1])

print('' .join(str(i) for i in reserved_array))
    





