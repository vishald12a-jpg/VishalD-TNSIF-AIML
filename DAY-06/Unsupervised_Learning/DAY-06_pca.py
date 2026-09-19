import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X = np.array([
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12],
    [5, 10, 15],
    [6, 12, 18]
])

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Original Shape:", X.shape)
print("PCA Shape:", X_pca.shape)
print("\nPCA Result:")
print(X_pca)

print("\nExplained Variance:")
print(pca.explained_variance_ratio_)

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title("PCA Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()