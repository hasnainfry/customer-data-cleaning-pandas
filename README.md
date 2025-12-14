# customer-data-cleaning-pandas
Customer data cleaning and exploratory analysis using Python and Pandas.
# Customer Data Cleaning & Exploratory Analysis

## 📌 Project Overview
This project demonstrates a real-world data cleaning and exploratory analysis workflow using Python and Pandas.  
The dataset contains customer information including missing values, duplicates, and inconsistencies.  
The project focuses on cleaning the data, generating insights, and preparing a final cleaned dataset.

## 🧰 Tools Used
- Python
- Pandas
- NumPy

## 🧹 Data Cleaning Steps
1. Checked for missing values in all columns.
2. Interpolated missing values in `age`.
3. Filled missing `purchases` with mean value.
4. Filled missing `city` with `"sao_pablo"`.
5. Dropped rows where `total_amount` is missing.
6. Identified and removed duplicate records based on `customer_id` and `name`.

## 📊 Data Insights
- Total purchases by city.
- Average total_amount by city.
- Top 3 customers by total spending.
- City-wise customer distribution in percentage.
- Filtered customers based on age and purchases criteria.

## 💾 Final Cleaned Data
The final cleaned dataset contains:
- `customer_id`
- `name`
- `age`
- `city`
- `purchases`
- `total_amount`

Saved as `cleaned.csv`.

## 🚀 Usage
1. Clone the repository.
2. Run the `data_cleaning.ipynb` or `.py` file.
3. The cleaned dataset `cleaned.csv` will be created in the specified folder.

## 📝 Author
Aspiring Data Analyst
