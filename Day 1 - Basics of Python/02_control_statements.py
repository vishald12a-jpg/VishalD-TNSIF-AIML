# If Statement
age = 10
if age < 18:
    print("Not Eligible")

# If-Else Statement
age = 20
if age <= 18:
    print("Not Eligible")
else:
    print("Eligible")

# Elif Statement
marks = int(input("Enter the mark: "))
if marks >= 90 and marks <= 100:
    print("Grade O")
elif marks >= 80 and marks < 90:
    print("Grade A")
else:
    print("Fail")