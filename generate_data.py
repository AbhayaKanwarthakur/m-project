import pandas as pd
import numpy as np

np.random.seed(42)

n = 2000

temperature = np.random.uniform(30, 150, n)
rpm = np.random.uniform(1000, 10000, n)
vibration = np.random.uniform(0.1, 5.0, n)
stress = np.random.uniform(50, 500, n)

failure = (
    (temperature > 110) &
    (rpm > 7000) &
    (vibration > 3) &
    (stress > 350)
).astype(int)

df = pd.DataFrame({
    "temperature": temperature,
    "rpm": rpm,
    "vibration": vibration,
    "stress": stress,
    "failure": failure
})

df.to_csv("data/rotating_disk_data.csv", index=False)

print("Dataset generated.")