import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file path
file_path = "C:/Users/Sinvha/data/Leads.csv"

def load_data(path):
    """Loads the dataset and handles errors."""
    if not os.path.exists(path):
        print("❌ Error: File not found! Check the file path.")
        return None
    return pd.read_csv(path)

def clean_data(df):
    """Handles missing values and ensures numeric columns stay numeric."""
    for col in df.columns:
        if df[col].dtype == "object":  # If it's a text column
            df[col].fillna("Unknown", inplace=True)  
        else:  # If it's a numeric column
            df[col].fillna(0, inplace=True)  # Replace NaN with 0 for numbers
    return df

def generate_lead_score(df):
    """Creates a basic lead scoring system after ensuring numeric values."""
    numeric_columns = ["Total Time Spent on Website", "Page Views Per Visit", "Converted"]
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert to numbers, set errors to NaN
    
    df["lead_score"] = (
        df["Total Time Spent on Website"].fillna(0) * 0.3 +
        df["Page Views Per Visit"].fillna(0) * 0.2 +
        df["Converted"].fillna(0) * 0.5
    )
    
    return df

def visualize_lead_activity(df):
    """Plots the distribution of lead activities."""
    df["Last Notable Activity"].value_counts().plot(kind="bar", figsize=(10, 5))
    plt.title("Lead Activity Distribution")
    plt.xlabel("Activity Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# Main execution
df = load_data(file_path)

if df is not None:
    df = clean_data(df)
    df = generate_lead_score(df)
    print("✅ Dataset Processed Successfully!")
    print(df.head())  # Show first few rows
    visualize_lead_activity(df)  # Show visualization
