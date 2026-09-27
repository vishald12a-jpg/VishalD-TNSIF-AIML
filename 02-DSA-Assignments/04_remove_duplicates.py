arr = [10, 20, 10, 30, 20, 40, 30]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print("Original Array:", arr)
print("Array after removing duplicates:", result)