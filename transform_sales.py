import pandas as pd
import re

# Load datasets
sales_df = pd.read_csv("sales.csv")
products_df = pd.read_csv("products.csv")

# Step 1: Extract product_code using regex
def extract_product_code(description):
    pattern = r'[A-Z]{2}-\d{4}-[A-Z]{2}'  # Pattern matching product codes
    match = re.search(pattern, description)
    return match.group(0) if match else None

sales_df['product_code'] = sales_df['description'].apply(extract_product_code)

# Step 2: Match product_code with product_name
merged_df = sales_df.merge(
    products_df[['product_code', 'product_name']],
    on='product_code',
    how='left'
)

# Save transformed sales file
merged_df.to_csv("output/updated_sales.csv", index=False)

# Step 3: Calculate total sales by category
# Merge category information into the sales data
merged_df = merged_df.merge(
    products_df[['product_code', 'category']],
    on='product_code',
    how='left'
)

# Group by category and calculate total sales
category_summary = merged_df.groupby('category')['amount'].sum().reset_index()
category_summary.rename(columns={'amount': 'total_sales'}, inplace=True)

# Save category summary
category_summary.to_csv("output/category_summary.csv", index=False)

# Print outputs for verification
print("Transformed Sales Data:")
print(merged_df[['transaction_id', 'description', 'amount', 'product_name']])
print("\nCategory-Wise Sales Summary:")
print(category_summary)
