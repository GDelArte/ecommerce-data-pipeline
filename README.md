# E-commerce Data Pipeline (Olist)

## Objective
Transform raw Olist datasets into a final, analysis-ready dataset by applying merges, aggregations, and business logic using Python and Pandas.

## Datasets Used
Located in `data/raw/`:
- Orders, customers, items, payments, and others.

## ETL Workflow
1. Read all CSV files
2. Merge orders with customers
3. Aggregate items and payments
4. Generate the final dataset `final_orders.csv`
5. Save the processed data in `data/processed/`

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt

