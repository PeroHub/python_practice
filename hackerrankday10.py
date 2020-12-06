"""Task
Given a base-10 integer, n, convert it to binary (base-). Then find and print 10 the base- integer denoting the maximum number of consecutive 1's in 's binary representation. When working with different bases, it is common to show the base as a subscript."""

n = int(input())

current_consecutive_no = 0
max_consecutive_no = 0
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_no += 1
        if current_consecutive_no > max_consecutive_no:
            max_consecutive_no = current_consecutive_no
        
    else:
        current_consecutive_no = 0
    n = n // 2
print(max_consecutive_no)
