arr = [10, -5, 20, -8, 15, -2]

positive_sum = 0
negative_sum = 0

for num in arr:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num

print("Positive Sum:", positive_sum)
print("Negative Sum:", negative_sum)