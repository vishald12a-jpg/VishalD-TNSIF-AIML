from fastapi import FastAPI
from pydantic import BaseModel
import joblib


# ============================================================
# 1. CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="Customer Persona Segmentation API",
    description="API for predicting customer personas using K-Means clustering",
    version="1.0.0"
)


# ============================================================
# 2. LOAD TRAINED MODEL, SCALER AND PERSONA MAPPING
# ============================================================

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")
persona_mapping = joblib.load("persona_mapping.pkl")


# ============================================================
# 3. INPUT DATA MODEL
# ============================================================

class CustomerData(BaseModel):
    annual_income_k: float
    spending_score: float


# ============================================================
# 4. ROOT ENDPOINT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Customer Persona Segmentation API is running"
    }


# ============================================================
# 5. HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# ============================================================
# 6. PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_persona(customer: CustomerData):

    # Create input using the same feature order
    input_data = [[
        customer.annual_income_k,
        customer.spending_score
    ]]

    # Apply the trained scaler
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    cluster = int(kmeans.predict(input_scaled)[0])

    # Get persona name
    persona = persona_mapping[cluster]

    # Return JSON response
    return {
        "annual_income_k": customer.annual_income_k,
        "spending_score": customer.spending_score,
        "cluster": cluster,
        "persona": persona
    }