# ============================================================
# CKD STAGE PREDICTION - STREAMLIT APP
# ============================================================

import pandas as pd
import streamlit as st
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CKD Stage Prediction",
    page_icon="🩺",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

# app.py is inside:
# mlcdk/app/app.py
#
# parent.parent points to:
# mlcdk/

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "ckd_severity_random_forest.pkl"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = None

try:
    model = joblib.load(MODEL_PATH)

except Exception as e:
    st.error(
        f"❌ Error loading model: {e}"
    )

    st.info(
        f"Expected model location:\n\n{MODEL_PATH}"
    )


# ============================================================
# HEADER
# ============================================================

st.title("🩺 Chronic Kidney Disease Stage Prediction")

st.write(
    "Enter the patient's clinical and laboratory details "
    "to estimate the CKD stage."
)


if model is not None:
    st.success("✅ Model loaded successfully!")


# ============================================================
# PATIENT INFORMATION
# ============================================================

st.markdown("---")

st.header("👤 Patient Information")

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# Column 1
# ------------------------------------------------------------

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=22.5,
        step=0.1
    )


# ------------------------------------------------------------
# Column 2
# ------------------------------------------------------------

with col2:

    diabetes = st.selectbox(
        "Diabetes",
        ["No", "Yes"]
    )

    hypertension = st.selectbox(
        "Hypertension",
        ["No", "Yes"]
    )

    smoking = st.selectbox(
        "Smoking Status",
        ["No", "Yes"]
    )

    family_history = st.selectbox(
        "Family History of Kidney Disease",
        ["No", "Yes"]
    )


# ============================================================
# VITAL SIGNS
# ============================================================

st.markdown("---")

st.header("❤️ Vital Signs")

col3, col4 = st.columns(2)


with col3:

    systolic_bp = st.number_input(
        "Systolic Blood Pressure (mmHg)",
        min_value=50,
        max_value=250,
        value=120
    )

    diastolic_bp = st.number_input(
        "Diastolic Blood Pressure (mmHg)",
        min_value=30,
        max_value=150,
        value=80
    )


with col4:

    heart_rate = st.number_input(
        "Heart Rate (bpm)",
        min_value=30,
        max_value=200,
        value=72
    )


# ============================================================
# BLOOD TEST PARAMETERS
# ============================================================

st.markdown("---")

st.header("🩸 Blood Test Parameters")

col5, col6 = st.columns(2)


with col5:

    serum_creatinine = st.number_input(
        "Serum Creatinine (mg/dL)",
        min_value=0.0,
        max_value=20.0,
        value=1.0,
        step=0.1
    )

    blood_urea_nitrogen = st.number_input(
        "Blood Urea Nitrogen (mg/dL)",
        min_value=0.0,
        max_value=200.0,
        value=20.0,
        step=0.1
    )

    egfr = st.number_input(
        "eGFR (mL/min/1.73m²)",
        min_value=0.0,
        max_value=150.0,
        value=90.0,
        step=0.1
    )

    sodium = st.number_input(
        "Sodium (mEq/L)",
        min_value=100.0,
        max_value=170.0,
        value=140.0,
        step=0.1
    )

    potassium = st.number_input(
        "Potassium (mEq/L)",
        min_value=2.0,
        max_value=8.0,
        value=4.5,
        step=0.1
    )


with col6:

    calcium = st.number_input(
        "Calcium (mg/dL)",
        min_value=5.0,
        max_value=15.0,
        value=9.5,
        step=0.1
    )

    phosphorus = st.number_input(
        "Phosphorus (mg/dL)",
        min_value=1.0,
        max_value=10.0,
        value=4.0,
        step=0.1
    )

    chloride = st.number_input(
        "Chloride (mEq/L)",
        min_value=80.0,
        max_value=130.0,
        value=100.0,
        step=0.1
    )

    bicarbonate = st.number_input(
        "Bicarbonate (mEq/L)",
        min_value=5.0,
        max_value=40.0,
        value=24.0,
        step=0.1
    )

    hemoglobin = st.number_input(
        "Hemoglobin (g/dL)",
        min_value=5.0,
        max_value=20.0,
        value=13.5,
        step=0.1
    )


# ============================================================
# URINE TEST PARAMETERS
# ============================================================

st.markdown("---")

st.header("🚽 Urine Test Parameters")

col7, col8 = st.columns(2)


with col7:

    urine_albumin = st.number_input(
        "Urine Albumin (mg/dL)",
        min_value=0.0,
        max_value=1000.0,
        value=20.0,
        step=0.1
    )

    urine_protein = st.number_input(
        "Urine Protein (mg/dL)",
        min_value=0.0,
        max_value=1000.0,
        value=30.0,
        step=0.1
    )

    acr = st.number_input(
        "Albumin-Creatinine Ratio (mg/g)",
        min_value=0.0,
        max_value=5000.0,
        value=30.0,
        step=0.1
    )


with col8:

    urine_specific_gravity = st.number_input(
        "Urine Specific Gravity",
        min_value=1.000,
        max_value=1.050,
        value=1.020,
        step=0.001,
        format="%.3f"
    )


# ============================================================
# BLOOD CELL COUNTS
# ============================================================

st.markdown("---")

st.header("🩸 Blood Cell Counts")

col9, col10 = st.columns(2)


with col9:

    rbc_count = st.number_input(
        "RBC Count (million/µL)",
        min_value=0.0,
        max_value=10.0,
        value=4.5,
        step=0.1
    )

    wbc_count = st.number_input(
        "WBC Count (/µL)",
        min_value=0,
        max_value=30000,
        value=7000,
        step=100
    )

    platelet_count = st.number_input(
        "Platelet Count (/µL)",
        min_value=0,
        max_value=1000000,
        value=250000,
        step=1000
    )


with col10:

    packed_cell_volume = st.number_input(
        "Packed Cell Volume (%)",
        min_value=10.0,
        max_value=70.0,
        value=42.0,
        step=0.1
    )


# ============================================================
# GLUCOSE PROFILE
# ============================================================

st.markdown("---")

st.header("🍬 Glucose Profile")

col11, col12 = st.columns(2)


with col11:

    blood_glucose_random = st.number_input(
        "Random Blood Glucose (mg/dL)",
        min_value=40.0,
        max_value=600.0,
        value=120.0,
        step=1.0
    )

    fasting_glucose = st.number_input(
        "Fasting Glucose (mg/dL)",
        min_value=40.0,
        max_value=400.0,
        value=95.0,
        step=1.0
    )


with col12:

    hba1c = st.number_input(
        "HbA1c (%)",
        min_value=3.0,
        max_value=20.0,
        value=5.5,
        step=0.1
    )


# ============================================================
# LIPID & PROTEIN PROFILE
# ============================================================

st.markdown("---")

st.header("🧪 Lipid & Protein Profile")

col13, col14 = st.columns(2)


with col13:

    cholesterol = st.number_input(
        "Total Cholesterol (mg/dL)",
        min_value=50.0,
        max_value=500.0,
        value=180.0,
        step=1.0
    )

    triglycerides = st.number_input(
        "Triglycerides (mg/dL)",
        min_value=20.0,
        max_value=1000.0,
        value=150.0,
        step=1.0
    )


with col14:

    serum_albumin = st.number_input(
        "Serum Albumin (g/dL)",
        min_value=1.0,
        max_value=6.0,
        value=4.0,
        step=0.1
    )

    total_protein = st.number_input(
        "Total Protein (g/dL)",
        min_value=3.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )


# ============================================================
# PREDICTION
# ============================================================

st.markdown("---")

st.header("🔍 CKD Stage Prediction")


if st.button(
    "🔍 Predict CKD Stage",
    use_container_width=True
):

    if model is None:

        st.error(
            "❌ Prediction cannot be performed because "
            "the model was not loaded."
        )

    else:

        try:

            # ------------------------------------------------
            # Encode categorical variables
            # ------------------------------------------------

            gender_encoded = (
                1 if gender == "Male" else 0
            )

            diabetes_encoded = (
                1 if diabetes == "Yes" else 0
            )

            hypertension_encoded = (
                1 if hypertension == "Yes" else 0
            )

            smoking_encoded = (
                1 if smoking == "Yes" else 0
            )

            family_history_encoded = (
                1 if family_history == "Yes" else 0
            )


            # ------------------------------------------------
            # Create input dataframe
            # ------------------------------------------------

            input_data = pd.DataFrame({

                "Age": [age],

                "Gender": [gender_encoded],

                "BMI": [bmi],

                "Systolic_BP": [systolic_bp],

                "Diastolic_BP": [diastolic_bp],

                "Heart_Rate": [heart_rate],

                "Serum_Creatinine": [
                    serum_creatinine
                ],

                "Blood_Urea_Nitrogen": [
                    blood_urea_nitrogen
                ],

                "eGFR": [egfr],

                "Urine_Albumin": [
                    urine_albumin
                ],

                "Urine_Protein": [
                    urine_protein
                ],

                "Albumin_Creatinine_Ratio": [
                    acr
                ],

                "Urine_Specific_Gravity": [
                    urine_specific_gravity
                ],

                "Sodium": [sodium],

                "Potassium": [potassium],

                "Calcium": [calcium],

                "Phosphorus": [phosphorus],

                "Chloride": [chloride],

                "Bicarbonate": [bicarbonate],

                "Hemoglobin": [hemoglobin],

                "RBC_Count": [rbc_count],

                "WBC_Count": [wbc_count],

                "Platelet_Count": [
                    platelet_count
                ],

                "Packed_Cell_Volume": [
                    packed_cell_volume
                ],

                "Blood_Glucose_Random": [
                    blood_glucose_random
                ],

                "Fasting_Glucose": [
                    fasting_glucose
                ],

                "HbA1c": [hba1c],

                "Cholesterol": [
                    cholesterol
                ],

                "Triglycerides": [
                    triglycerides
                ],

                "Serum_Albumin": [
                    serum_albumin
                ],

                "Total_Protein": [
                    total_protein
                ],

                "Diabetes": [
                    diabetes_encoded
                ],

                "Hypertension": [
                    hypertension_encoded
                ],

                "Smoking_Status": [
                    smoking_encoded
                ],

                "Family_History_Kidney": [
                    family_history_encoded
                ]
            })


            # ------------------------------------------------
            # Prediction
            # ------------------------------------------------

            prediction = model.predict(input_data)[0]


            # ------------------------------------------------
            # Stage Names
            # ------------------------------------------------

            stage_names = {

                0: "Stage 1",

                1: "Stage 2",

                2: "Stage 3",

                3: "Stage 4",

                4: "Stage 5"
            }


            predicted_stage = stage_names.get(
                prediction,
                str(prediction)
            )


            # ------------------------------------------------
            # Stage Descriptions
            # ------------------------------------------------

            stage_description = {

                0:
                "🟢 Stage 1: Kidney function is "
                "normal or near normal.",

                1:
                "🟡 Stage 2: Mild reduction "
                "in kidney function.",

                2:
                "🟠 Stage 3: Moderate reduction "
                "in kidney function.",

                3:
                "🔴 Stage 4: Severe reduction "
                "in kidney function.",

                4:
                "⚫ Stage 5: Kidney failure."
            }


            # ------------------------------------------------
            # Display Prediction
            # ------------------------------------------------

            st.success(
                f"### 🩺 Predicted CKD Stage: "
                f"{predicted_stage}"
            )


            # ------------------------------------------------
            # Display Probability
            # ------------------------------------------------

            if hasattr(model, "predict_proba"):

                probabilities = (
                    model.predict_proba(input_data)[0]
                )

                max_probability = max(
                    probabilities
                )

                st.metric(
                    "Model Confidence",
                    f"{max_probability * 100:.2f}%"
                )


                st.subheader(
                    "📊 Stage Probability"
                )

                probability_data = pd.DataFrame({

                    "Stage": [
                        stage_names.get(
                            cls,
                            str(cls)
                        )
                        for cls in model.classes_
                    ],

                    "Probability": [
                        f"{prob * 100:.2f}%"
                        for prob in probabilities
                    ]
                })

                st.dataframe(
                    probability_data,
                    use_container_width=True,
                    hide_index=True
                )


            # ------------------------------------------------
            # Description
            # ------------------------------------------------

            st.info(
                stage_description.get(
                    prediction,
                    "No description available."
                )
            )


        except Exception as e:

            st.error(
                f"❌ Prediction error: {e}"
            )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.warning(
    """
    ⚠️ **Important Disclaimer**

    This application is an educational/research machine-learning
    prototype. It is not a medical diagnostic device and should not
    replace evaluation, laboratory testing, or advice from a qualified
    healthcare professional.
    """
)