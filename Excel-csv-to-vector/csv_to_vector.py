import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load CSV file
file_path = "/Users/apurvpandey/Documents/ALL Repos/LLM-With-Tabular-Data/data/csv/A_Z_medicines_dataset_of_India.csv"  # Change this to your actual file path
df = pd.read_csv(file_path)

# Initialize text embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert CSV data into embeddings
text_data = df.astype(str).apply(lambda x: " ".join(x), axis=1).tolist()
embeddings = model.encode(text_data, convert_to_numpy=True)

# Create FAISS index
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "pharma_items_faiss.index")

print("Vector database (FAISS) created successfully!")