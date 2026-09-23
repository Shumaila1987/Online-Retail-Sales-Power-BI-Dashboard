import pandas as pd
df = pd.read_csv("online_retail_II_raw.csv")
print(f"Total rows: {len(df)}")
print(df.columns.tolist())
print(df.head())
import pandas as pd

# Load data
df = pd.read_csv("online_retail_II_raw.csv")

# Show initial info
print(f"✅ Original shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Step 1 — Remove missing values
df = df.dropna()
print(f"✅ After removing blanks: {df.shape[0]} rows")

# Step 2 — Remove cancelled orders (Invoice starts with 'C')
df = df[~df['Invoice'].astype(str).str.startswith('C')]
print(f"✅ After removing cancelled orders: {df.shape[0]} rows")

# Step 3 — Keep only positive Quantity & Price
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]
print(f"✅ After removing negatives: {df.shape[0]} rows")

# Step 4 — Calculate Total Sales
df['TotalSales'] = df['Quantity'] * df['Price']

# Step 5 — Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Step 6 — Add Year, Month, Day columns
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month_name()
df['Day'] = df['InvoiceDate'].dt.day_name()

# Show cleaned data summary
print("\n📊 CLEANED DATA PREVIEW:")
print(df[['Invoice', 'Quantity', 'Price', 'TotalSales', 'InvoiceDate', 'Country']].head())
print(f"\n💰 Total Sales: £{df['TotalSales'].sum():,.2f}")
# Save cleaned data for Power BI
df.to_csv("online_retail_cleaned.csv", index=False)
print("\n✅ Cleaned data saved as: online_retail_cleaned.csv")

# --- QUICK ANALYSIS ---
print("\n" + "="*50)
print("📈 KEY INSIGHTS")
print("="*50)

# Sales by Country
print("\n🌍 Top 5 Countries by Sales:")
country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head()
print(country_sales.round(2))

# Sales by Month
print("\n📅 Sales by Month:")
month_sales = df.groupby('Month')['TotalSales'].sum().sort_values(ascending=False)
print(month_sales.round(2))

# Top Products
print("\n🛍️ Top 5 Products by Sales:")
product_sales = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head()
print(product_sales.round(2))

print("\n✅ ALL DONE! Open 'online_retail_cleaned.csv' in Excel & Power BI next!")