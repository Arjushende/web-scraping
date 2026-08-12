import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD DATA
# ==========================================

df = pd.read_csv("books.csv")


# ==========================================
# STEP 2: CLEAN PRICE
# ==========================================

df["Price"] = df["Price"].str.replace("Â£", "", regex=False)
df["Price"] = df["Price"].astype(float)


# ==========================================
# STEP 3: CHECK DATA
# ==========================================

print("===== FIRST 5 BOOKS =====")
print(df.head())


# ==========================================
# STEP 4: BAR CHART
# ==========================================

plt.figure(figsize=(12, 6))

plt.bar(df["Title"][:10], df["Price"][:10])

plt.title("Price of First 10 Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")

plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("book_prices_bar_chart.png")

plt.show()


# ==========================================
# STEP 5: HISTOGRAM
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(df["Price"], bins=10)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig("book_price_distribution.png")

plt.show()


# ==========================================
# STEP 6: HORIZONTAL BAR CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.barh(df["Title"][:10], df["Price"][:10])

plt.title("Book Prices - First 10 Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.tight_layout()

plt.savefig("book_prices_horizontal.png")

plt.show()


# ==========================================
# STEP 7: LINE CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(df["Price"], marker="o")

plt.title("Book Price Variation")
plt.xlabel("Book Number")
plt.ylabel("Price (£)")

plt.tight_layout()

plt.savefig("book_price_variation.png")

plt.show()


# ==========================================
# STEP 8: DATA INSIGHTS
# ==========================================

average_price = df["Price"].mean()
minimum_price = df["Price"].min()
maximum_price = df["Price"].max()

print("\n===== DATA INSIGHTS =====")

print("Average Price:", average_price)
print("Minimum Price:", minimum_price)
print("Maximum Price:", maximum_price)


# ==========================================
# STEP 9: CHEAPEST & MOST EXPENSIVE BOOK
# ==========================================

cheapest_book = df.loc[df["Price"].idxmin()]
most_expensive_book = df.loc[df["Price"].idxmax()]

print("\n===== CHEAPEST BOOK =====")
print(cheapest_book)

print("\n===== MOST EXPENSIVE BOOK =====")
print(most_expensive_book)


print("\n===================================")
print("DATA VISUALIZATION COMPLETED!")
print("===================================")