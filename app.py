import streamlit as st
import pickle
import pandas as pd

with open("failure_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Structural Health Monitoring Dashboard")

st.write("Predict failure risk in rotating disk systems")

temperature = st.slider(
    "Temperature (°C)",
    30.0,
    150.0,
    80.0
)

rpm = st.slider(
    "RPM",
    1000,
    10000,
    5000
)

vibration = st.slider(
    "Vibration",
    0.1,
    5.0,
    2.0
)

stress = st.slider(
    "Stress (MPa)",
    50.0,
    500.0,
    200.0
)

if st.button("Predict Failure Risk"):

    data = pd.DataFrame({
        "temperature": [temperature],
        "rpm": [rpm],
        "vibration": [vibration],
        "stress": [stress]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(
            f"High Failure Risk ({probability:.2%})"
        )
    else:
        st.success(
            f"Low Failure Risk ({probability:.2%})"
        )