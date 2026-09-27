arr = [10, 5, 0, 7, 8, 0, 13, 4]

even = 0
odd = 0
zero = 0

for num in arr:
    if num == 0:
        zero += 1
    elif num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print("Zero:", zero)