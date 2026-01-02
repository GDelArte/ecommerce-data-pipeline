import pandas as pd
from pathlib import Path


def extract_orders(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "olist_orders_dataset.csv")


def extract_customers(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "olist_customers_dataset.csv")


def extract_items(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "olist_order_items_dataset.csv")


def extract_payments(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "olist_order_payments_dataset.csv")

