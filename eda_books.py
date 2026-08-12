import pandas as pd

# ==========================================
# STEP 1: LOAD THE DATASET
# ==========================================

df = pd.read_csv("books.csv")

print("Dataset loaded successfully!")


# ==========================================
# STEP 2: CLEAN THE PRICE COLUMN
# ==========================================

# Remove Â£ symbol
df["Price"] = df["Price"].str.replace("Â£", "", regex=False)

# Convert Price from text to number
df["Price"] = df["Price"].astype(float)


# ==========================================
# STEP 3: EXPLORE DATA STRUCTURE
# ==========================================

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== LAST 5 ROWS =====")
print(df.tail())

print("\n===== DATASET SHAPE =====")
print("Rows and Columns:", df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== DATA TYPES =====")
print(df.dtypes)


# ==========================================
# STEP 4: MISSING VALUES
# ==========================================

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# ==========================================
# STEP 5: SUMMARY STATISTICS
# ==========================================

print("\n===== SUMMARY STATISTICS =====")
print(df["Price"].describe())


# ==========================================
# STEP 6: AVERAGE PRICE
# ==========================================

average_price = df["Price"].mean()

print("\n===== AVERAGE PRICE =====")
print("Average book price:", average_price)


# ==========================================
# STEP 7: CHEAPEST BOOK
# ==========================================

cheapest = df.loc[df["Price"].idxmin()]

print("\n===== CHEAPEST BOOK =====")
print(cheapest)


# ==========================================
# STEP 8: MOST EXPENSIVE BOOK
# ==========================================

most_expensive = df.loc[df["Price"].idxmax()]

print("\n===== MOST EXPENSIVE BOOK =====")
print(most_expensive)


# ==========================================
# STEP 9: DUPLICATE ROWS
# ==========================================

duplicates = df.duplicated().sum()

print("\n===== DUPLICATE ROWS =====")
print("Number of duplicate rows:", duplicates)


# ==========================================
# STEP 10: INVALID PRICES
# ==========================================

print("\n===== INVALID PRICES =====")

zero_prices = (df["Price"] == 0).sum()
negative_prices = (df["Price"] < 0).sum()

print("Zero prices:", zero_prices)
print("Negative prices:", negative_prices)


# ==========================================
# STEP 11: OUTLIER DETECTION
# ==========================================

print("\n===== OUTLIER DETECTION =====")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)


# Find outliers
outliers = df[
    (df["Price"] < lower_bound) |
    (df["Price"] > upper_bound)
]

print("\n===== OUTLIER BOOKS =====")
print(outliers)


# ==========================================
# STEP 12: SIMPLE HYPOTHESIS CHECK
# ==========================================

print("\n===== HYPOTHESIS TEST =====")

print("Hypothesis: Is the average book price greater than £35?")

if average_price > 35:
    print("Result: Average book price is greater than £35.")
else:
    print("Result: Average book price is not greater than £35.")


# ==========================================
# FINAL MESSAGE
# ==========================================

print("\n===================================")
print("EDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("===================================")