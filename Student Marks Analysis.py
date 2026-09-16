import numpy as np

marks = np.array([65, 78, 90, 55, 82, 74, 95, 68, 88, 45])

print("Student Marks:")
print(marks)

print("\nTotal Marks:", np.sum(marks))

print("Average Marks:", np.mean(marks))

print("Highest Mark:", np.max(marks))

print("Lowest Mark:", np.min(marks))

print("\nMarks Greater Than 75:")
print(marks[marks > 75])