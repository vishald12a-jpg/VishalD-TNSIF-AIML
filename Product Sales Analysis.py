import pandas as pd

data = {
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 800, 1500, 12000, 2500],
    "Quantity Sold": [20, 80, 60, 35, 70]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Sales Data:")
print(df)

print("\nProduct with Highest Sales:")
print(df[df["Total Sales"] == df["Total Sales"].max()])

print("\nAverage Product Price:")
print(df["Price"].mean())

print("\nProducts with Quantity Sold Greater Than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts Sorted by Total Sales:")
print(df.sort_values("Total Sales", ascending=False))