import pandas as pd
import re
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Step 1: Load datasets
def load_data():
    try:
        sales_df = pd.read_csv("sales.csv")
        products_df = pd.read_csv("products.csv")
        return sales_df, products_df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

# Step 2: Extract product_code using regex
def extract_product_code(description):
    pattern = r'[A-Z]{2}-\d{4}-[A-Z]{2}'  # Product code format
    match = re.search(pattern, description)
    return match.group(0) if match else None

def add_product_code_column(sales_df):
    sales_df['product_code'] = sales_df['description'].apply(extract_product_code)
    return sales_df

# Step 3: Merge with products.csv to add product_name
def merge_product_name(sales_df, products_df):
    return sales_df.merge(
        products_df[['product_code', 'product_name']],
        on='product_code',
        how='left'
    )

# Step 4: Calculate category-wise sales summary
def calculate_category_summary(merged_df, products_df):
    merged_with_category = merged_df.merge(
        products_df[['product_code', 'category']],
        on='product_code',
        how='left'
    )
    category_summary = merged_with_category.groupby('category')['amount'].sum().reset_index()
    category_summary.rename(columns={'amount': 'total_sales'}, inplace=True)
    return category_summary

# Step 5: Save outputs
def save_outputs(merged_df, category_summary):
    # Save the transformed sales file
    merged_df.to_csv("output/updated_sales.csv", index=False)
    print("Transformed sales data saved to 'output/updated_sales.csv'")
    
    # Save the category summary file
    category_summary.to_csv("output/category_summary.csv", index=False)
    print("Category-wise sales summary saved to 'output/category_summary.csv'")

# Main function
def main():
    # Load data
    sales_df, products_df = load_data()

    # Process data
    sales_df = add_product_code_column(sales_df)
    merged_df = merge_product_name(sales_df, products_df)
    category_summary = calculate_category_summary(merged_df, products_df)

    # Save results
    save_outputs(merged_df, category_summary)

    # Print results for quick verification
    print("\nTransformed Sales Data:")
    print(merged_df[['transaction_id', 'description', 'amount', 'product_name']])
    print("\nCategory-Wise Sales Summary:")
    print(category_summary)

# Entry point
if __name__ == "__main__":
    main()
