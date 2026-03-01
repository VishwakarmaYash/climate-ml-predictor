import joblib
import sys
import os
import pandas as pd

# Load model
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "model.pkl")
model = joblib.load(model_path)

if len(sys.argv) != 2:
    print("Usage: python predict.py <year>")
    sys.exit()

year = int(sys.argv[1])

# ✅ Create DataFrame with same column name used during training
input_df = pd.DataFrame({'Year': [year]})

prediction = model.predict(input_df)

print(f"Predicted Temperature for {year}: {prediction[0]:.2f} °C")