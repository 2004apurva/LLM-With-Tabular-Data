import pandas as pd
from sqlalchemy import create_engine
import os

# Define file paths
csv_file = "/Users/apurvpandey/Documents/Office_Work_Personal/Tabular_data_handling/data/csv/A_Z_medicines_dataset_of_India.csv"  # Replace with actual file path
save_folder = "/Users/apurvpandey/Documents/Office_Work_Personal/Tabular_data_handling/SQL"  # Replace with your folder path

# Ensure the folder exists
os.makedirs(save_folder, exist_ok=True)

# Define full path for SQLite database
sqlite_db = os.path.join(save_folder, "Medicine_data.db")

# Load Excel file
df = pd.read_csv(csv_file)

# Create SQLite database engine
engine = create_engine(f"sqlite:///{sqlite_db}")

# Convert DataFrame to SQLite
df.to_sql("Medicine_data", con=engine, if_exists="replace", index=False)

print(f"Excel file successfully converted to SQLite database!\nSaved at: {sqlite_db}")