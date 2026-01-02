from src.etl.extract import extract_orders
from pathlib import Path

def test_extract():
    data_dir = Path("../../data/raw")  # caminho relativo até os CSVs
    df = extract_orders(data_dir)
    print(df.head())

if __name__ == "__main__":
    test_extract()
