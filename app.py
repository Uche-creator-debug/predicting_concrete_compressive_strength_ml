import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.base import BaseEstimator, TransformerMixin

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Concrete Strength Predictor",
    page_icon="🏗️",
    layout="wide"
)

# -------------------------------------------------------
# Feature Engineering Class
# -------------------------------------------------------

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y = None):
        return self
    def transform(self, X):
        X = X.copy()
        X['water_cement_ratio'] = X['water'] / X['cement']
        X['binders'] = X['ash'] + X['slag'] + X['cement']
        X["water_binders_ratio"] = X['water'] / X['binders']
        X["total_aggregates"] = X['coarseagg'] + X['fineagg']
        X["total_aggregates_ratio"] = X['total_aggregates'] / X['cement']
        X["age"] = np.log1p(X["age"])
        return X


# -------------------------------------------------------
# Load Model
# -------------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("./models/concrete_strength_model.joblib")


try:
    model = load_model()
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(e)
    st.stop()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.title("🏗️ About")

    st.write(
        """
This application predicts the **compressive strength of concrete**
using an optimized **XGBoost** machine learning model.

### Model Performance

- **MAE:** 2.38 MPa
- **RMSE:** 3.63 MPa
- **R²:** 0.95

The model was trained using engineering-informed feature engineering,
Optuna hyperparameter tuning, and SHAP explainability.
"""
    )

    st.markdown("---")

    st.write(
        """
Developed by **Uche**

Civil Engineering × Machine Learning
"""
    )

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🏗️ Concrete Compressive Strength Predictor")

st.write(
"""
Predict the compressive strength of concrete based on its mix proportions
using an optimized **XGBoost** machine learning model.
"""
)

st.markdown("---")

# -------------------------------------------------------
# Input Layout
# -------------------------------------------------------

left, right = st.columns(2)

with left:

    cement = st.number_input(
        "Cement (kg/m³)",
        100.0,
        600.0,
        250.0
    )

    slag = st.number_input(
        "Blast Furnace Slag (kg/m³)",
        0.0,
        400.0,
        0.0
    )

    ash = st.number_input(
        "Fly Ash (kg/m³)",
        0.0,
        300.0,
        0.0
    )

    water = st.number_input(
        "Water (kg/m³)",
        100.0,
        250.0,
        180.0
    )

with right:

    superplastic = st.number_input(
        "Superplasticizer (kg/m³)",
        0.0,
        50.0,
        0.0
    )

    coarseagg = st.number_input(
        "Coarse Aggregate (kg/m³)",
        800.0,
        1200.0,
        1000.0
    )

    fineagg = st.number_input(
        "Fine Aggregate (kg/m³)",
        500.0,
        1000.0,
        700.0
    )

    age = st.number_input(
        "Age (Days)",
        1,
        365,
        28
    )

# -------------------------------------------------------
# Engineering Features
# -------------------------------------------------------

binder = cement + slag + ash
total_agg = coarseagg + fineagg

water_cement = water / cement

water_binder = water / binder if binder != 0 else np.nan

aggregate_ratio = total_agg / cement

st.markdown("## 📊 Mix Summary")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Binder Content", f"{binder:.1f} kg/m³")

m2.metric("Water/Cement", f"{water_cement:.2f}")

m3.metric("Water/Binder", f"{water_binder:.2f}")

m4.metric("Total Aggregates", f"{total_agg:.1f} kg/m³")

st.markdown("---")

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

if st.button("🔍 Predict Compressive Strength"):

    input_df = pd.DataFrame([{
        "cement": cement,
        "slag": slag,
        "ash": ash,
        "water": water,
        "superplastic": superplastic,
        "coarseagg": coarseagg,
        "fineagg": fineagg,
        "age": age
    }])

    prediction = model.predict(input_df)[0]

    st.success("Prediction Complete!")

    st.metric(
        "Predicted Compressive Strength",
        f"{prediction:.2f} MPa"
    )

    # Classification

    if prediction < 20:
        grade = "🟡 Low Strength Concrete"

    elif prediction < 40:
        grade = "🟢 Normal Strength Concrete"

    elif prediction < 60:
        grade = "🔵 High Strength Concrete"

    else:
        grade = "🟣 High-Performance Concrete"

    st.info(f"### Classification: {grade}")

# -------------------------------------------------------
# About Model
# -------------------------------------------------------

with st.expander("ℹ️ About this Model"):

    st.write(
        """
### Machine Learning Workflow

- Exploratory Data Analysis (EDA)
- Engineering-informed Feature Engineering
- Linear Regression Baseline
- Multiple ML Models
- Hyperparameter Optimization using Optuna
- Final Tuned XGBoost Model
- SHAP Explainability

The engineered features include:

- Water-Cement Ratio
- Water-Binder Ratio
- Total Binder Content
- Total Aggregate Ratio

These features capture important concrete technology principles and
significantly improved model performance.
"""
    )

st.markdown("---")

st.caption(
    "© 2026 | Concrete Strength Prediction using Machine Learning"
)