import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [10, 11, 12],
    [11, 12, 13],
    [12, 13, 14],
    [20, 21, 22],
    [21, 22, 23],
    [22, 23, 24]
])

tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=3
)

X_tsne = tsne.fit_transform(X)

print("t-SNE Result:")
print(X_tsne)

plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.title("t-SNE Visualization")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()