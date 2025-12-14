import pandas as pd

# Load messy data
df = pd.read_csv("messy_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicate rows
df = df.drop_duplicates()

# Clean salary column
df["salary"] = df["salary"].replace("[₹,]", "", regex=True)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Clean age column
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Handle missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["gender"] = df["gender"].str.lower().str.strip()
df["gender"] = df["gender"].replace({"m": "male", "f": "female"})
df["city"] = df["city"].fillna("Unknown")

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed successfully.")
