import pandas as pd
from sqlalchemy import create_engine
import os

# Define file paths
excel_file = "/Users/apurvpandey/Documents/Office_Work_Personal/Tabular_data_handling/data/xl/ROUTE_OF_PHARMA_ITEMS.xlsx"  # Replace with actual file path
save_folder = "/Users/apurvpandey/Documents/Office_Work_Personal/Tabular_data_handling/SQL"  # Replace with your folder path

# Ensure the folder exists
os.makedirs(save_folder, exist_ok=True)

# Define full path for SQLite database
sqlite_db = os.path.join(save_folder, "pharma_items.db")

# Load Excel file
df = pd.read_excel(excel_file, engine="openpyxl")

# Create SQLite database engine
engine = create_engine(f"sqlite:///{sqlite_db}")

# Convert DataFrame to SQLite
df.to_sql("pharma_items", con=engine, if_exists="replace", index=False)

print(f"Excel file successfully converted to SQLite database!\nSaved at: {sqlite_db}")