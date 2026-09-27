arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n

rotated = arr[-k:] + arr[:-k]

print("Original Array:", arr)
print("Array after right rotation:", rotated)