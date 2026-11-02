# ==========================================================
#  OTT Subscriber Churn - Simple EDA
#  (Put this file in the same folder as the CSV and run it)
# ==========================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Folder to save the charts
os.makedirs("charts", exist_ok=True)


# ----------------------------------------------------------
# STEP 1: Load the data
# ----------------------------------------------------------
df = pd.read_csv("ott_subscriber_churn_for EDA.csv")

print("Rows and columns:", df.shape)
print(df.head())
print(df.info())


# ----------------------------------------------------------
# STEP 2: Check the problems in the data
# ----------------------------------------------------------
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
print("\nGender values:", df["gender"].unique())
print("City values:", df["city"].nunique())
print("\nAge min and max:", df["age"].min(), df["age"].max())
print("Watch hours max:", df["watch_hours_month"].max())


# ----------------------------------------------------------
# STEP 3: Clean the data
# ----------------------------------------------------------
# 3.1 Remove duplicate rows
df = df.drop_duplicates()

# 3.2 Fix gender (M -> Male, F -> Female)
df["gender"] = df["gender"].replace({"M": "Male", "F": "Female"})

# 3.3 Fix city names (remove spaces and make first letter capital)
df["city"] = df["city"].str.strip().str.title()

# 3.4 Wrong ages (like -1 or 999) -> make them empty
df.loc[df["age"] < 10, "age"] = None
df.loc[df["age"] > 100, "age"] = None

# 3.5 Fill empty numbers with the middle value (median)
df["age"] = df["age"].fillna(df["age"].median())
df["watch_hours_month"] = df["watch_hours_month"].fillna(df["watch_hours_month"].median())
df["avg_content_rating"] = df["avg_content_rating"].fillna(df["avg_content_rating"].median())

# 3.6 Fill empty text columns with "Unknown"
df["payment_method"] = df["payment_method"].fillna("Unknown")
df["primary_device"] = df["primary_device"].fillna("Unknown")

# 3.7 Cut very big watch hours (limit = 99th percentile)
limit = df["watch_hours_month"].quantile(0.99)
df["watch_hours_month"] = df["watch_hours_month"].clip(upper=limit)

# 3.8 Make new columns by grouping numbers into ranges
df["tenure_group"] = pd.cut(df["tenure_months"],
                            bins=[0, 6, 12, 24, 40],
                            labels=["0-6 months", "7-12 months", "13-24 months", "25+ months"])

df["login_gap_group"] = pd.cut(df["days_since_last_login"],
                               bins=[-1, 3, 7, 14, 100],
                               labels=["0-3 days", "4-7 days", "8-14 days", "15+ days"])

print("\nAfter cleaning:", df.shape)
print("Missing values left:", df.isnull().sum().sum())

# Save the cleaned data
df.to_csv("ott_churn_cleaned.csv", index=False)


# ----------------------------------------------------------
# STEP 4: Overall churn rate
# ----------------------------------------------------------
# churned is 1 (left) or 0 (stayed), so the average is the churn rate
churn_rate = df["churned"].mean() * 100
print("\nOverall churn rate: %.2f%%" % churn_rate)

df["churned"].value_counts().plot(kind="bar")
plt.title("Churned (1) vs Stayed (0)")
plt.xlabel("Churned")
plt.ylabel("Number of customers")
plt.savefig("charts/1_churn_count.png")
plt.show()
plt.close()


# ----------------------------------------------------------
# STEP 5: Churn rate by each group
# ----------------------------------------------------------
group_columns = ["subscription_plan", "payment_method", "primary_device",
                 "city", "tenure_group", "login_gap_group"]

for col in group_columns:
    rates = df.groupby(col)["churned"].mean() * 100
    rates = rates.sort_values()
    print("\nChurn % by", col)
    print(rates.round(2))

    rates.plot(kind="barh")
    plt.title("Churn % by " + col)
    plt.xlabel("Churn %")
    plt.savefig("charts/2_churn_by_" + col + ".png")
    plt.show()
    plt.close()


# ----------------------------------------------------------
# STEP 6: Compare churned and stayed customers (averages)
# ----------------------------------------------------------
number_columns = ["age", "tenure_months", "watch_hours_month", "sessions_month",
                  "days_since_last_login", "support_tickets", "avg_content_rating"]

print("\nAverage values (0 = stayed, 1 = churned):")
print(df.groupby("churned")[number_columns].mean().round(2))

sns.boxplot(data=df, x="churned", y="support_tickets")
plt.title("Support tickets: stayed vs churned")
plt.savefig("charts/3_tickets_boxplot.png")
plt.show()
plt.close()


# ----------------------------------------------------------
# STEP 7: Which numbers are linked to churn? (correlation)
# ----------------------------------------------------------
numbers = df[number_columns + ["monthly_fee_inr", "discount_pct", "churned"]]
correlation = numbers.corr()

print("\nCorrelation with churn:")
print(correlation["churned"].sort_values())

plt.figure(figsize=(9, 7))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("charts/4_correlation.png")
plt.show()
plt.close()


# ----------------------------------------------------------
# STEP 8: Final summary
# ----------------------------------------------------------
print("\nDONE. Cleaned file and charts are saved.")
