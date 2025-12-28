import pandas as pd
import os
import shutil

def csv_to_excel():
    csv_path = "data/mizan_benchmark.csv"
    excel_path = "data/mizan_benchmark.xlsx"
    public_docs_path = "docs/public/mizan_benchmark.xlsx"
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    print(f"Reading {csv_path}...")
    df = pd.read_csv(csv_path)
    
    print(f"Converting to {excel_path}...")
    df.to_excel(excel_path, index=False)
    
    # Ensure public folder exists
    os.makedirs(os.path.dirname(public_docs_path), exist_ok=True)
    
    # Copy to docs/public for direct download link
    print(f"Copying to {public_docs_path} for website download...")
    shutil.copy2(excel_path, public_docs_path)
    
    print("Done! Excel file is ready in /data and /docs/public.")

if __name__ == "__main__":
    csv_to_excel()
