

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/home/ayyan/lib/BestSeller_Books_of_Amazon.csv')

# Clean the Price column and remove duplicates
df['Price'] = df['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)
df.drop_duplicates(inplace=True)

# --- Analysis ---

# 1. Descriptive Statistics
print('Descriptive Statistics:')
print(df.describe())

# 2. Top Authors
print('\nTop Authors:')
print(df['Author Name'].value_counts().head(10))

# 3. Visualizations
plt.figure(figsize=(12, 6))

# Price Distribution
plt.subplot(1, 2, 1)
plt.hist(df['Price'], bins=20)
plt.title('Price Distribution')
plt.xlabel('Price (₹)')
plt.ylabel('Frequency')


# Rating Distribution
plt.subplot(1, 2, 2)
plt.hist(df['Rating'], bins=20)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')

plt.tight_layout()
# Save the first figure
plt.savefig('/home/ayyan/lib/distributions.png')
print("\nSaved price and rating distribution plot to distributions.png")


# Price vs. Rating Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Price'], df['Rating'])
plt.title('Price vs. Rating')
plt.xlabel('Price (₹)')
plt.ylabel('Rating')

# Save the second figure
plt.savefig('/home/ayyan/lib/price_vs_rating.png')
print("Saved price vs rating scatter plot to price_vs_rating.png")

# Save the cleaned data
df.to_csv('/home/ayyan/lib/cleaned_bestsellers.csv', index=False)
print("Saved cleaned data to cleaned_bestsellers.csv")

