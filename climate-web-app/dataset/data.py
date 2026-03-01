import pandas as pd

data_path = r"C:\Users\BHARAT\Downloads\archive.zip"
df = pd.read_csv(data_path)

print("Original Shape:", df.shape)

print("\nMissing Values:\n", df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)
df.drop_duplicates(inplace=True)

# Rename columns for easier ML usage
df.rename(columns={
    "Avg Temperature (°C)": "Temperature",
    "CO2 Emissions (Tons/Capita)": "CO2",
    "Sea Level Rise (mm)": "Sea_Level",
    "Rainfall (mm)": "Rainfall",
    "Renewable Energy (%)": "Renewable_Energy",
    "Forest Area (%)": "Forest_Area"
}, inplace=True)

# Select features
df = df[['Year', 'Temperature']]

print("\nCleaned Shape:", df.shape)

df.to_csv("cleaned_climate_data.csv", index=False)

print("\nPreprocessing Completed ✅")