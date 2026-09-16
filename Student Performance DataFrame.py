import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Charan", "Deepak", "Ezhil", "Farhan", "Gokul", "Hari"],
    "Department": ["CSE", "IT", "CSE", "ECE", "CSE", "IT", "ECE", "CSE"],
    "Marks": [85, 72, 91, 68, 77, 88, 59, 95],
    "Attendance": [90, 85, 78, 92, 75, 88, 95, 80]
}

df = pd.DataFrame(data)

print("First 5 Students:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nStudents with Marks Greater Than 75:")
print(df[df["Marks"] > 75])

print("\nStudents with Attendance Below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents Sorted by Marks:")
print(df.sort_values("Marks"))