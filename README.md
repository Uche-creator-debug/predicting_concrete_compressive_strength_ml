# Concrete Compressive Strength Prediction using Machine Learning

Predicting the compressive strength of concrete is a fundamental task in civil engineering, as it helps engineers assess the quality and structural performance of concrete before construction. This project develops a machine learning model capable of predicting concrete compressive strength based on mix proportions and curing age. 

The workflow includes exploratory data analysis (EDA), feature engineering, model comparison, hyperparameter optimization with Optuna, model explainability using SHAP, and deployment as an interactive Streamlit web application.

## 🚀 Project Overview

This project demonstrates an end-to-end machine learning workflow for predicting the compressive strength of concrete. The objective was to build a highly accurate and interpretable regression model while incorporating engineering knowledge through feature engineering.

**Final Model Performance (Unseen Test Set):**
| Metric | Value |
| :--- | :--- |
| **MAE** | 2.38 MPa |
| **RMSE** | 3.63 MPa |
| **R²** | 0.95 |

The model explains approximately 95% of the variability in concrete compressive strength while maintaining a relatively low prediction error.

---

## 📊 Dataset

The dataset contains 1,030 concrete mix designs, each described using eight input variables and one target variable.

### Features
| Feature | Description |
| :--- | :--- |
| **Cement** | Cement content (kg/m³) |
| **Slag** | Blast furnace slag (kg/m³) |
| **Ash** | Fly ash (kg/m³) |
| **Water** | Water content (kg/m³) |
| **Superplasticizer**| Superplasticizer content (kg/m³) |
| **Coarse Aggregate**| Coarse aggregate (kg/m³) |
| **Fine Aggregate** | Fine aggregate (kg/m³) |
| **Age** | Concrete curing age (days) |

### Target
* **Concrete Compressive Strength** (MPa)

---

## 🔍 Exploratory Data Analysis (EDA)

Several exploratory analyses were conducted to better understand the dataset:

**Distribution Analysis:**
* Concrete strength is approximately normally distributed with a slight positive skew.
* Cement exhibits a moderate positive skew.
* Slag, fly ash, and superplasticizer are heavily right-skewed, indicating that they are absent or used sparingly in many mixes.
* Water and aggregate contents are comparatively more symmetric.
* Age is heavily skewed toward younger curing ages.

**Correlation Analysis:**
* **Cement** positively correlates with compressive strength.
* **Water** negatively correlates with strength.
* **Age** positively influences concrete strength.
* **Superplasticizer** contributes positively to strength.
* **Aggregate contents** exhibit relatively weak negative relationships.

---

## 🛠 Feature Engineering

Engineering knowledge was incorporated into the model by creating additional features, which substantially improved predictive performance.

### Engineered Features
| Feature | Description |
| :--- | :--- |
| **Water–Cement Ratio** | Water divided by cement content |
| **Binder Content** | Cement + Slag + Fly Ash |
| **Water–Binder Ratio** | Water divided by total binder content |
| **Total Aggregates** | Coarse + Fine Aggregate |
| **Aggregate Ratio** | Total Aggregates divided by Cement |
| **Log(Age)** | Logarithmic transformation of curing age |

**Key Outcomes:**
* **Water–Binder Ratio** became the strongest negative predictor.
* **Binder Content** became the strongest positive predictor.
* **Log-transformed Age** better captured the nonlinear strength gain over time.

---

## 🤖 Machine Learning Models

Several regression algorithms were evaluated against a Linear Regression baseline. Tree-based ensemble models significantly outperformed the baseline.

| Model | MAE | RMSE | R² |
| :--- | :--- | :--- | :--- |
| **Random Forest** | 3.27 | 5.21 | 0.896 |
| **XGBoost** | 3.03 | 5.27 | 0.893 |
| **Gradient Boosting** | 3.60 | 5.45 | 0.886 |
| **K-Nearest Neighbors** | 4.70 | 6.42 | 0.841 |
| **Decision Tree** | 4.64 | 7.44 | 0.787 |
| **Linear Regression (Baseline)** | 5.84 | 7.95 | 0.757 |
| **Support Vector Machine** | 5.72 | 8.03 | 0.752 |

### Hyperparameter Optimization
Optuna was used to optimize both Random Forest and XGBoost. The optimized **XGBoost** model achieved the best validation performance and was selected as the final model.

---

## 🧠 Model Explainability (SHAP)

SHAP analysis was performed to understand how the model makes predictions. The most influential features were:
1. Age
2. Water–Binder Ratio
3. Binder Content
4. Water–Cement Ratio
5. Water

The SHAP results align closely with established concrete technology principles:
* Older concrete generally develops higher strength.
* Increasing the water–binder ratio reduces strength.
* Higher binder content increases strength.
* Lower water content generally improves compressive strength.

---

## 💻 Streamlit Application

A Streamlit web application was developed to allow users to interactively predict concrete compressive strength. 

**Features:**
* Enter concrete mix proportions.
* Predict compressive strength instantly.
* View engineered mix characteristics.
* Classify predicted concrete strength.

---

## 📂 Repository Structure

```text
concrete-compressive-strength-prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── concrete.csv
│
├── models/
│   └── concrete_strength_model.joblib
│
├── notebooks/
│   ├── concrete-compressive-strength-project
│
└── images/

---

## Installation

- Clone the repository

-- git clone https://github.com/yourusername/concrete-compressive-strength-prediction.git

-Navigate into the project

-- cd concrete-compressive-strength-prediction

- Install dependencies

-- pip install -r requirements.txt

- Run the Streamlit application

-- streamlit run app.py

---


## Future Improvements

Potential enhancements include:

Deep learning models for comparison
Model uncertainty estimation
Batch prediction using CSV uploads
Mix optimization to achieve a target strength
Concrete strength prediction intervals
Docker containerization and cloud deployment
Integration with engineering design workflows

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Optuna
- SHAP
- Matplotlib
- Plotly
- Streamlit

---


## References
- Yeh, I. C. (1998). Modeling of Strength of High-Performance Concrete Using Artificial Neural Networks.
UCI Machine Learning Repository – Concrete Compressive Strength Dataset.
- Scikit-learn Documentation.
- XGBoost Documentation.
- Optuna Documentation.
- SHAP Documentation.

---

### Author

**Uche**

Civil Engineering Graduate | Machine Learning Enthusiast | Incoming MSc Structural Engineering Student

Passionate about applying machine learning, finite element analysis, and data-driven techniques to solve civil and structural engineering problems.
