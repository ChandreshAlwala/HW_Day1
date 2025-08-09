# Write a program to take 5 numbers from the user and store them in a tuple, then print the
# maximum and minimum.
# Take exactly 5 numbers from the user
num = tuple(map(int, input("Enter 5 numbers separated by space: ").split()))

if len(num) != 5:
    print("Please enter exactly 5 numbers!")
else:
    print("Tuple:", num)
    print("Maximum:", max(num))
    print("Minimum:", min(num))


