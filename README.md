# m-project
Structural Health Monitoring Dashboard
# AI-Based Structural Health Monitoring for Rotating Disk Systems

## Overview

This project presents an AI-driven Structural Health Monitoring (SHM) system for rotating disk components. The system predicts potential structural failures using machine learning based on operational parameters such as temperature, rotational speed (RPM), vibration, and stress.

The project was inspired by research in Physics-Informed AI for structural failure prediction and demonstrates how data-driven techniques can assist in predictive maintenance and reliability assessment of engineering systems.

---

## Features

- Failure risk prediction using Machine Learning
- Interactive Streamlit dashboard
- Synthetic engineering dataset generation
- Random Forest classification model
- Real-time user input and prediction
- Easy-to-extend architecture for research applications

---

## Project Structure

```text
structural-health-monitoring/
│
├── app.py
├── train_model.py
├── generate_data.py
├── failure_model.pkl
├── requirements.txt
├── README.md
│
└── data/
    └── rotating_disk_data.csv
```

---

## Input Parameters

The model uses the following operational parameters:

| Parameter | Description |
|------------|------------|
| Temperature | Operating temperature (°C) |
| RPM | Rotational speed |
| Vibration | Vibration amplitude |
| Stress | Mechanical stress (MPa) |

---

## Machine Learning Model

The project uses a Random Forest Classifier to identify whether a rotating disk is operating under safe conditions or approaching a failure state.

### Workflow

1. Generate synthetic operational data
2. Train Random Forest model
3. Save trained model
4. Deploy using Streamlit dashboard
5. Predict failure probability in real time

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/structural-health-monitoring.git
cd structural-health-monitoring
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Generate Dataset

```bash
python generate_data.py
```

---

## Train Model

```bash
python train_model.py
```

---

## Launch Dashboard

```bash
streamlit run app.py
```

---

## Example Dashboard Output

The dashboard provides:

- Failure prediction
- Failure probability score
- Risk assessment visualization

Example:

```
Temperature: 120°C
RPM: 8500
Vibration: 4.1
Stress: 420 MPa

Prediction:
High Failure Risk (92%)
```

---

## Future Improvements

- Physics-Informed Neural Networks (PINNs)
- Remaining Useful Life (RUL) prediction
- Real sensor integration
- Explainable AI using SHAP
- Finite Element Analysis (FEA) coupling
- Time-series anomaly detection
- Edge deployment for industrial monitoring

---

## Applications

- Aerospace systems
- Turbine monitoring
- Rotating machinery diagnostics
- Predictive maintenance
- Industrial reliability engineering
- Structural health monitoring research

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

---

## Author

Abhaya Kanwar

Research Interests:
- Artificial Intelligence
- Machine Learning
- Physics-Informed AI
- Structural Health Monitoring
- Astrophysics

---

## License

This project is released under the MIT License.