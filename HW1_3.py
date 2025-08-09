num = int(input("Enter the 4 digit no:"))
total =0
for digits in str(num):
  total += int(digits)
print(total)