import pandas as pd 

df = pd.read_csv("/storage/emulated/0/Download/repo.csv")

# Cleaning 
print ("Missing Values Finding & Cleaning ")

# Age interpolate
df["age"] = df["age"].interpolate()


# Purchases mean fill
df["purchases"] = df["purchases"].fillna(df["purchases"].mean())


# City missing fill
df["city"] = df["city"].fillna("not_ provide")
print(df["city"])

# Drop rows with missing total_amount
df.dropna(subset=["total_amount"], inplace=True)
print(df) 

# Find duplicates
print (df.duplicated())

# Remove duplicates based on customer_id + name
df.drop_duplicates(subset=["customer_id","name"], inplace=True)


## Insights 
print ("Make some insight")

# City-wise total purchases
city_total_purchases = df.groupby("city")["purchases"].sum()
print(city_total_purchases)

# City-wise average total_amount
city_avg_amount = df.groupby("city")["total_amount"].mean()
print(city_avg_amount)

# Dataset summary
print(df.describe())

### Filtering
print ("filtering")

# Filter: age > 30 AND total_amount > 30000
filtered1 = df.loc[(df["age"] > 30) & (df["total_amount"] > 30000),["name","age","total_amount"]]
print(filtered1)

# Top 3 customers by total_amount
top3 = df.sort_values(by="total_amount", ascending=False).head(3)
print(top3)

# City distribution 
city_percent = df["city"].value_counts(normalize=True) * 100
print(city_percent)

# Filter: age < 30 AND purchases < 4
filtered2 = df.loc[(df["age"] < 30) & (df["purchases"] < 4),["name","city","purchases"]]
print(filtered2)

#### Final Cleaned Data frame
print ("Final Cleaned CSV")


final_df = df[["customer_id","name","age","city","purchases","total_amount"]]
print (final_df)

# Save Your Data 

final_df.to_csv("cleaned.csv", index = False)

