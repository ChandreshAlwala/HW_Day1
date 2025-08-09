# Given a tuple of integers, write a program to count how many elements are divisible by
# 3.
num = (1,3,6,2,9)
count =0
for i in num:
    if(i % 3 ==0):
        count += 1

print(count)