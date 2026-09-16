import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 160, 210, 240]

# Line Chart
plt.figure(figsize=(7, 4))

plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()


# Bar Chart
plt.figure(figsize=(7, 4))

plt.bar(months, sales, label="Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

plt.show()