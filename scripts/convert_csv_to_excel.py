import pandas as pd
import os

def csv_to_excel():
    csv_path = "data/mizan_benchmark.csv"
    excel_path = "data/mizan_benchmark.xlsx"
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    print(f"Reading {csv_path}...")
    df = pd.read_csv(csv_path)
    
    print(f"Converting to {excel_path}...")
    df.to_excel(excel_path, index=False)
    print("Done!")

if __name__ == "__main__":
    csv_to_excel()
