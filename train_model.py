import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("dataset.csv")

X = df[[
    "CAN_ID",
    "DLC",
    "DATA_SUM"
]]

model = IsolationForest()

model.fit(X)

joblib.dump(
    model,
    "model.pkl"
)

print("Model Trained")