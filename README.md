# Data Transformation and Analysis

## Overview
This project performs data transformation and analysis on two datasets: `sales.csv` and `products.csv`. The script extracts product codes from sales descriptions, matches them with product names, and calculates category-wise sales summaries.

---

## File Structure

```
.venv/
|
├── sales.csv        # Input sales data
├── products.csv     # Input products data
├── main.py          # Main script for processing
|-- transform_sales.py          
└── output/
    ├── updated_sales.csv    # Transformed sales file with product_name
    └── category_summary.csv # Category-wise sales summary
```

---

## Steps to Run the Project

### 1. Prepare Input Files
Ensure the following files are present in the project directory:
- `sales.csv`: Contains sales transaction data with descriptions.
- `products.csv`: Contains product details including product codes, names, and categories.

### 2. Install Dependencies
This project uses Python and requires the `pandas` library. Install it by running:
```bash
pip install pandas
```

### 3. Run the Script
Execute the main script to perform the transformations and generate outputs:
```bash
python main.py
```

---

## Outputs

### 1. Transformed Sales Data (`output/updated_sales.csv`)
This file includes a new column, `product_name`, mapped from `products.csv` based on the extracted product codes.

| transaction_id | description                                 | amount | product_code | product_name       |
|----------------|---------------------------------------------|--------|--------------|--------------------|
| T001           | Bought Smart Watch (SW-1234-AB)            | 199.99 | SW-1234-AB   | Smart Watch        |
| T002           | Purchased Wireless Earbuds WE-5678-CD      | 99.99  | WE-5678-CD   | Wireless Earbuds   |
| T003           | Running Shoes - RS9012EF                  | 149.99 | RS-9012-EF   | Running Shoes      |
| T004           | Bluetooth Speaker (BS-3456-GH)            | 49.99  | BS-3456-GH   | Bluetooth Speaker  |
| T005           | Sneakers Casual, Code: CS-7890-IJ          | 79.99  | CS-7890-IJ   | Casual Sneakers    |

### 2. Category-Wise Sales Summary (`output/category_summary.csv`)
This file contains the total sales for each category based on the `category` column in `products.csv`.

| category    | total_sales |
|-------------|-------------|
| Electronics | 349.97      |
| Footwear    | 229.98      |

---
## Script Explanation
### Step-by-Step Process
#### 1. Load Datasets
The script reads the input files `sales.csv` and `products.csv` into pandas DataFrames.
#### 2. Extract Product Codes
Using a regular expression, the script extracts product codes in the format `XX-XXXX-XX` from the `description` column in `sales.csv`.
#### 3. Map Product Names
The extracted product codes are matched with the `product_code` column in `products.csv` to retrieve the corresponding `product_name`. This is added as a new column in the sales dataset.
#### 4. Category-Wise Summary
The script calculates the total sales amount for each category by joining the sales data with the `category` column from `products.csv`.
#### 5. Save Outputs
The transformed sales data and category summary are saved as CSV files in the `output/` folder.
---
## Example Input Files
### `products.csv`
| product_id | product_name       | product_code | category    |
|------------|--------------------|--------------|-------------|
| 101        | Smart Watch        | SW-1234-AB   | Electronics |
| 102        | Wireless Earbuds  | WE-5678-CD   | Electronics |
| 103        | Running Shoes     | RS-9012-EF   | Footwear    |
| 104        | Bluetooth Speaker | BS-3456-GH   | Electronics |
| 105        | Casual Sneakers   | CS-7890-IJ   | Footwear    |
### `sales.csv`
| transaction_id | description                                 | amount |
|----------------|---------------------------------------------|--------|
| T001           | Bought Smart Watch (SW-1234-AB)            | 199.99 |
| T002           | Purchased Wireless Earbuds WE-5678-CD      | 99.99  |
| T003           | Running Shoes - RS9012EF                  | 149.99 |
| T004           | Bluetooth Speaker (BS-3456-GH)            | 49.99  |
| T005           | Sneakers Casual, Code: CS-7890-IJ          | 79.99  |

---
## Notes
- Ensure the product codes in `sales.csv` descriptions strictly follow the format `XX-XXXX-XX`.
- If a product code is not found in `products.csv`, the `product_name` column will have a `NaN` value.
---

## Troubleshooting

1. **FileNotFoundError**: Verify that `sales.csv` and `products.csv` are in the correct directory.
2. **Empty Outputs**: Check the product code format in `sales.csv` descriptions for consistency.
3. **Dependency Issues**: Ensure that `pandas` is installed in your Python environment.
---
## Contact
For further assistance, feel free to reach out to the project owner.
