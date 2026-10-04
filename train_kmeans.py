import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("customers.csv")

print("===== DATASET LOADED =====")
print("Shape:", df.shape)
print(df.head())


# ============================================================
# 2. SELECT FEATURES
# ============================================================

features = ["annual_income_k", "spending_score"]

X = df[features]

print("\n===== FEATURES USED FOR CLUSTERING =====")
print(features)


# ============================================================
# 3. STANDARDIZE FEATURES
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\n===== STANDARDIZATION COMPLETED =====")


# ============================================================
# 4. ELBOW METHOD
# ============================================================

inertias = []

for k in range(2, 8):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertias.append(model.inertia_)


plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 8),
    inertias,
    marker="o"
)

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.grid(True)

plt.savefig("elbow_method.png")
plt.show()


# ============================================================
# 5. SILHOUETTE SCORE
# ============================================================

print("\n===== SILHOUETTE SCORES =====")

scores = {}

for k in range(2, 8):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    scores[k] = score

    print(f"K = {k} → Silhouette Score = {score:.4f}")


# ============================================================
# 6. TRAIN FINAL K-MEANS MODEL
# ============================================================

n_clusters = 3

kmeans = KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)

df["cluster"] = kmeans.fit_predict(X_scaled)

print("\n===== K-MEANS TRAINING COMPLETED =====")
print("Number of clusters:", n_clusters)


# ============================================================
# 7. CLUSTER ANALYSIS
# ============================================================

print("\n===== CLUSTER ANALYSIS =====")

cluster_summary = df.groupby("cluster")[features].mean()

print(cluster_summary)


# ============================================================
# 8. PERSONA MAPPING
# ============================================================

persona_mapping = {}

for cluster in cluster_summary.index:

    income = cluster_summary.loc[cluster, "annual_income_k"]
    spending = cluster_summary.loc[cluster, "spending_score"]

    if income >= cluster_summary["annual_income_k"].mean() and \
       spending >= cluster_summary["spending_score"].mean():

        persona = "High-Value Customers"

    elif income < cluster_summary["annual_income_k"].mean() and \
         spending >= cluster_summary["spending_score"].mean():

        persona = "Budget-Conscious Customers"

    else:

        persona = "Low-Spending High-Income Customers"

    persona_mapping[cluster] = persona


df["persona"] = df["cluster"].map(persona_mapping)


# ============================================================
# 9. DISPLAY PERSONAS
# ============================================================

print("\n===== CUSTOMER PERSONAS =====")

for cluster, persona in persona_mapping.items():

    cluster_data = df[df["cluster"] == cluster]

    print(f"\nCluster {cluster}: {persona}")

    print(
        "Average Income:",
        round(cluster_data["annual_income_k"].mean(), 2)
    )

    print(
        "Average Spending:",
        round(cluster_data["spending_score"].mean(), 2)
    )

    print(
        "Customers:",
        len(cluster_data)
    )


# ============================================================
# 10. VISUALIZE CLUSTERS
# ============================================================

plt.figure(figsize=(8, 5))

for cluster in range(n_clusters):

    cluster_data = df[df["cluster"] == cluster]

    plt.scatter(
        cluster_data["annual_income_k"],
        cluster_data["spending_score"],
        label=persona_mapping[cluster],
        alpha=0.7
    )


# Plot cluster centers

centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.title("Customer Persona Segmentation")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.legend()
plt.grid(True)

plt.savefig(
    "customer_clusters.png"
)

plt.show()


# ============================================================
# 11. SAVE CLUSTERED DATA
# ============================================================

df.to_csv(
    "customers_clustered.csv",
    index=False
)

print("\n===== CLUSTERED DATA SAVED =====")


# ============================================================
# 12. SAVE MODEL
# ============================================================

joblib.dump(
    kmeans,
    "kmeans_model.pkl"
)

print("kmeans_model.pkl saved")


# ============================================================
# 13. SAVE SCALER
# ============================================================

joblib.dump(
    scaler,
    "scaler.pkl"
)

print("scaler.pkl saved")


# ============================================================
# 14. SAVE PERSONA MAPPING
# ============================================================

joblib.dump(
    persona_mapping,
    "persona_mapping.pkl"
)

print("persona_mapping.pkl saved")


# ============================================================
# FINAL
# ============================================================

print("\n========================================")
print("K-MEANS TRAINING COMPLETED SUCCESSFULLY")
print("========================================")

print("\nGenerated files:")
print("- customers_clustered.csv")
print("- kmeans_model.pkl")
print("- scaler.pkl")
print("- persona_mapping.pkl")
print("- elbow_method.png")
print("- customer_clusters.png")