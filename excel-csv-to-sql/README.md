# README: Convert CSV & Excel to SQLite Database

## Overview
This guide provides step-by-step instructions on converting **CSV and Excel files into an SQLite database** using Python. The process includes setting up the environment, running scripts, and verifying the database.

---

## 1️⃣ Prerequisites
Ensure you have Python installed and set up on your system.

### Install Required Libraries
Run the following command in your terminal:
```bash
pip install pandas sqlalchemy openpyxl
```
- **pandas**: Used for data handling.
- **sqlalchemy**: Helps in database connection.
- **openpyxl**: Required for handling Excel files.

---

## 2️⃣ Convert an Excel File (`.xlsx`) to SQLite

### Steps:
1. Place your Excel file (e.g., `ROUTE_OF_PHARMA_ITEMS.xlsx`) in a known directory.
2. Modify the script below to match your file path and destination folder.
3. Run the script to create an SQLite database.

### Python Script:
```python
import pandas as pd
from sqlalchemy import create_engine
import os

# Define file paths
excel_file = "ROUTE_OF_PHARMA_ITEMS.xlsx"  # Replace with actual file path
save_folder = "/Users/your_username/Documents/sqlite_db/"  # Replace with desired folder path

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
```

### Verify the SQLite Database:
After execution, navigate to the folder in your terminal and open SQLite:
```bash
cd /Users/your_username/Documents/sqlite_db/
sqlite3 pharma_items.db
```
Run SQLite queries:
```sql
.tables
SELECT * FROM pharma_items LIMIT 5;
```

---

## 3️⃣ Convert a CSV File (`.csv`) to SQLite

### Steps:
1. Place your CSV file (e.g., `ROUTE_OF_PHARMA_ITEMS.csv`) in a known directory.
2. Modify the script below to match your file path and destination folder.
3. Run the script to create an SQLite database.

### Python Script:
```python
import pandas as pd
from sqlalchemy import create_engine
import os

# Define file paths
csv_file = "ROUTE_OF_PHARMA_ITEMS.csv"  # Replace with actual file path
save_folder = "/Users/your_username/Documents/sqlite_db/"  # Replace with desired folder path

# Ensure the folder exists
os.makedirs(save_folder, exist_ok=True)

# Define full path for SQLite database
sqlite_db = os.path.join(save_folder, "pharma_items.db")

# Load CSV file
df = pd.read_csv(csv_file)

# Create SQLite database engine
engine = create_engine(f"sqlite:///{sqlite_db}")

# Convert DataFrame to SQLite
df.to_sql("pharma_items", con=engine, if_exists="replace", index=False)

print(f"CSV file successfully converted to SQLite database!\nSaved at: {sqlite_db}")
```

### Verify the SQLite Database:
After execution, navigate to the folder in your terminal and open SQLite:
```bash
cd /Users/your_username/Documents/sqlite_db/
sqlite3 pharma_items.db
```
Run SQLite queries:
```sql
.tables
SELECT * FROM pharma_items LIMIT 5;
```

---

## 4️⃣ Summary of Commands
| Conversion   | Command |
|---------------|-------------|
| Install dependencies | `pip install pandas sqlalchemy openpyxl` |
| Convert Excel to SQLite | Use provided Python script |
| Convert CSV to SQLite | Use provided Python script |
| Open SQLite database | `sqlite3 pharma_items.db` |
| Check tables in DB | `.tables` |
| Query first 5 rows | `SELECT * FROM pharma_items LIMIT 5;` |

---

## 5️⃣ Notes
- Modify the file paths based on your directory structure.
- The scripts will **automatically create the destination folder** if it does not exist.
- Ensure you have the correct permissions to write to the specified folder.

---

🚀 **Your SQLite database is now ready for use!** Let me know if you need any modifications.

