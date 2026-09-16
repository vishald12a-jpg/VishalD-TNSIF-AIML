import numpy as np

temperatures = np.array([28, 31, 29, 35, 32, 27, 34])

print("Temperatures:")
print(temperatures)

print("\nAverage Temperature:", np.mean(temperatures))

print("Highest Temperature:", np.max(temperatures))

print("Lowest Temperature:", np.min(temperatures))

print("\nTemperatures Above 30°C:")
print(temperatures[temperatures > 30])

updated_temperatures = temperatures + 2

print("\nUpdated Temperatures:")
print(updated_temperatures)