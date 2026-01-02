import pandas as pd
from pathlib import Path

# Pastas
data_dir = Path("data/raw")
processed_dir = Path("data/processed")
processed_dir.mkdir(exist_ok=True)

# Ler os CSVs
orders = pd.read_csv(data_dir / "olist_orders_dataset.csv")
customers = pd.read_csv(data_dir / "olist_customers_dataset.csv")
items = pd.read_csv(data_dir / "olist_order_items_dataset.csv")
payments = pd.read_csv(data_dir / "olist_order_payments_dataset.csv")

# Merge orders + customers
orders_customers = orders.merge(customers, on="customer_id", how="left")

# Agregar itens
items_agg = items.groupby("order_id").agg(
    total_items=("order_item_id", "count"),
    total_freight=("freight_value", "sum"),
    total_price_items=("price", "sum")
).reset_index()

# Agregar pagamentos
payments_agg = payments.groupby("order_id").agg(
    total_payments=("payment_value", "sum"),
    payment_count=("payment_type", "count")
).reset_index()

# Merge final
final_orders = orders_customers.merge(items_agg, on="order_id", how="left")
final_orders = final_orders.merge(payments_agg, on="order_id", how="left")

# Salvar
final_orders.to_csv(processed_dir / "final_orders.csv", index=False)

print("ETL finalizado! Dataset salvo em data/processed/final_orders.csv")
