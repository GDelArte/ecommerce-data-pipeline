# E-commerce Data Pipeline

## Project Overview
This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** using the **Olist dataset** from Kaggle. The goal is to transform raw e-commerce data into a clean, structured, and analytics-ready dataset.  

The project showcases **data extraction, cleaning, transformation, aggregation, and loading**, highlighting both **data engineering skills** and the ability to **structure a production-ready pipeline**.

- **Data source:** [Olist Dataset on Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)  
- **Technologies used:** Python, Pandas, NumPy, Jupyter Notebook  
- **Project type:** ETL pipeline for e-commerce data

---

## Project Structure
ecommerce-data-pipeline/
│
├─ README.md
├─ requirements.txt # Project dependencies
├─ data/
│ ├─ raw/ # Original raw datasets downloaded from Kaggle
│ └─ processed/ # Final processed dataset after ETL
├─ notebooks/ # Exploratory analysis (Jupyter Notebooks)
│ └─ explore_data.ipynb # Data exploration, cleaning, aggregation experiments
├─ src/ # Production-ready ETL scripts
│ ├─ etl/
│ │ ├─ extract.py # Extract raw data
│ │ ├─ transform.py # Data cleaning and transformation
│ │ ├─ load.py # Load processed data to final destination
│ │ └─ pipeline.py # Orchestrates the ETL process
│ └─ utils/
│ └─ helpers.py # Utility functions

---

## Key Notes on Jupyter Usage

- **Exploratory notebooks:**  
  The Jupyter notebook (`notebooks/explore_data.ipynb`) was used for **data exploration, understanding the dataset, testing cleaning techniques, and aggregating insights**. This allows rapid experimentation before implementing production-ready scripts.

- **Production-ready code:**  
  All reusable ETL logic has been moved into Python scripts in `src/etl/`. This separation demonstrates best practices:
  - Notebooks for exploration
  - Python scripts for **repeatable, automated ETL pipelines**

---

## ETL Pipeline Details

1. **Extract:**  
   Raw CSV files from `data/raw/` are read into Pandas DataFrames.

2. **Transform:**  
   - Cleaning missing or inconsistent data  
   - Aggregating order items, payments, and customer information  
   - Combining multiple tables into a single consolidated dataset  

3. **Load:**  
   - The final cleaned dataset is saved as `data/processed/final_orders.csv`  
   - Ready for analytics or dashboarding by business analysts

---

## How to Run the Pipeline

1. **Install dependencies**:

2. **Run ETL pipeline**:

3. **Check processed data**:

---

## Key Takeaways

- Demonstrates **data cleaning, transformation, and aggregation** in Python using Pandas and NumPy.  
- Shows how to **structure a production-ready ETL pipeline**, separating exploration (notebooks) from reusable scripts.  
- Prepares data for **analytics, dashboards, or reporting**.  
- Explains the usage of **Jupyter Notebook** for experimentation without affecting production-ready scripts.  

---

## Notes

- The project uses **Jupyter Notebook** primarily for exploration and testing.  
- All production-ready ETL scripts are in Python, ensuring that the pipeline can run **automatically, reproducibly, and in a modular way**.

