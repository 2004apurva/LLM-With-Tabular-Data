import pandas as pd
import chromadb

# Define file path (Change this to your actual file path)
file_path = "data/xl/ROUTE_OF_PHARMA_ITEMS.xlsx"  # Replace with "ROUTE_OF_PHARMA_ITEMS.csv" for CSV

# Load the data into a Pandas DataFrame
df = pd.read_excel(file_path, engine="openpyxl")  # Use pd.read_csv(file_path) for CSV

# Initialize ChromaDB Persistent Client (Creates a persistent database)
chroma_client = chromadb.PersistentClient(path="pharma_items_chroma_db")

# Create a new collection
collection = chroma_client.get_or_create_collection(name="pharma_items")

# Insert each row into ChromaDB
for i, row in df.iterrows():
    collection.add(
        ids=[str(i)],  # Unique ID for each row
        documents=[str(row.to_dict())]  # Convert row data to string format
    )

print("Data successfully inserted into ChromaDB and saved in 'pharma_items_chroma_db'!")