arr1 = [1, 2, 2, 3, 4]
arr2 = [4, 2, 1, 2, 3]

frequency1 = {}
frequency2 = {}

for num in arr1:
    frequency1[num] = frequency1.get(num, 0) + 1

for num in arr2:
    frequency2[num] = frequency2.get(num, 0) + 1

if frequency1 == frequency2:
    print("Arrays are Equal")
else:
    print("Arrays are Not Equal")