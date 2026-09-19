import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Print results
print("Cluster Labels:", labels)
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()