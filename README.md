# EDA_Prcatice-for-Data-Analytics
# OTT Subscriber Churn - Exploratory Data Analysis (Python)

A beginner-friendly EDA project that finds out **which OTT (streaming) subscribers leave, and why**.

- **Dataset:** 5,060 subscribers, 18 columns (age, city, plan, payment method, watch hours, support tickets, churn flag and more)
- **Tools:** Python, pandas, Matplotlib, Seaborn
- **Result:** about 1 in 5 customers churned (20.24%)

## Files in this project

| File | What it is |
|---|---|
| `eda_simple.py` | The full EDA script (run this) |
| `ott_subscriber_churn_for EDA.csv` | Raw dataset |
| `ott_churn_cleaned.csv` | Cleaned dataset (created by the script) |
| `charts/` | All charts saved as PNG (created by the script) |
| `OTT_Churn_EDA_Visualizations.pdf` | All charts in one PDF |
| `OTT_Churn_EDA_Practice_Guide.pdf` | Study guide with line-by-line explanation and practice questions |

## What the script does (8 steps)

1. Load the data
2. Check the problems in the data
3. Clean the data
4. Overall churn rate
5. Churn rate by group (plan, payment, device, city, tenure, inactivity)
6. Compare churned and stayed customers
7. Correlation (which numbers are linked to churn)
8. Save the cleaned file and the charts

## Data problems found and fixed

| Problem | Fix |
|---|---|
| 60 duplicate rows | Removed |
| Gender written as M, F, Male, Female | Changed to Male / Female / Other |
| 38 city spellings (MUMBAI, mumbai, "Mumbai ") | Cleaned to 10 cities |
| Wrong ages (-1 and 999) | Treated as missing |
| Missing age, rating, watch hours | Filled with the median |
| Missing payment method and device | Filled with "Unknown" |
| Extreme watch hours (up to 670 per month) | Capped at the 99th percentile |

## Key findings

- Mobile plan users churn the most (28.95%). Premium users churn the least (9.55%).
- Wallet payers churn at 28.53%, about 9 points higher than other payment methods.
- Customers inactive for 15+ days churn at 27.49%, against about 19-20% for the rest.
- Newer subscribers churn more. Customers with 25+ months of tenure churn the least (17.49%).
- Support tickets have the strongest link with churn (correlation +0.16). Churned customers raised 1.21 tickets on average vs 0.82 for those who stayed.
- Customers who watch more, have more sessions and give higher ratings are more likely to stay.
- Gender, age, genre and device make little difference.

Note: these are patterns in the data. They show a link, not proof of what causes churn.

## Business suggestions

- Offer upgrade deals to Mobile plan users.
- Send a re-engagement message before a user reaches 15 days without login.
- Improve support quality and track repeat tickets as an early warning.
- Check wallet payment failures and promote UPI auto-pay.
- Improve onboarding for new subscribers.

## How to run

1. Install the libraries:
   ```
   pip install pandas matplotlib seaborn
   ```
2. Keep `eda_simple.py` and the CSV file in the same folder.
3. Run:
   ```
   python eda_simple.py
   ```
4. Find the cleaned data and the `charts` folder in the same folder.

## Next steps

- Build a churn prediction model (Logistic Regression, Random Forest)
- Build a Power BI dashboard on the cleaned data
- Test the retention ideas above with an A/B test

## Author

Rizwan - Data Analytics graduate
LinkedIn: linkedin.com/in/rizwan-t-dataanalyst
GitHub: github.com/Rizwan877822
