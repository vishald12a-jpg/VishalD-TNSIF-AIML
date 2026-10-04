import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Persona Segmentation",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Customer Persona Segmentation")
st.write("Predict a customer's marketing persona using K-Means clustering.")


# -----------------------------
# Customer Input
# -----------------------------
st.sidebar.header("Customer Details")

annual_income = st.sidebar.number_input(
    "Annual Income (₹ Thousands)",
    min_value=10.0,
    max_value=200.0,
    value=50.0,
    step=1.0
)

spending_score = st.sidebar.number_input(
    "Spending Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

predict_button = st.sidebar.button("🔮 Predict Persona")


# -----------------------------
# Prediction
# -----------------------------
if predict_button:

    data = {
        "annual_income_k": annual_income,
        "spending_score": spending_score
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed successfully!")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Annual Income",
                    f"${result['annual_income_k']:.1f}K"
                )

            with col2:
                st.metric(
                    "Spending Score",
                    f"{result['spending_score']:.1f}"
                )

            with col3:
                st.metric(
                    "Cluster",
                    result["cluster"]
                )

            st.subheader("🎯 Customer Persona")

            st.info(
                f"**{result['persona']}**"
            )

        else:
            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to FastAPI. "
            "Make sure the backend is running on port 8000."
        )


# -----------------------------
# Dataset Visualization
# -----------------------------
st.divider()

st.subheader("📊 Customer Segmentation")

try:

    df = pd.read_csv("customers_clustered.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    personas = df["persona"].unique()

    for persona in personas:

        data = df[df["persona"] == persona]

        ax.scatter(
            data["annual_income_k"],
            data["spending_score"],
            label=persona,
            alpha=0.7
        )

    ax.set_xlabel("Annual Income (₹ Thousands)")
    ax.set_ylabel("Spending Score")
    ax.set_title("Customer Persona Clusters")
    ax.legend()

    st.pyplot(fig)

except Exception as e:

    st.warning(
        f"Could not load visualization data: {e}"
    )


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Unsupervised Learning • K-Means Customer Persona Segmentation"
)