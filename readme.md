# 🏦 Bank Loan Risk & Profitability Analytics

An end-to-end data analytics project focused on analyzing loan portfolio performance, borrower risk, default patterns, and loan characteristics using **Python, SQL, and Power BI**.

The project analyzes **1.34M+ loan records** to identify factors associated with loan defaults and create an interactive risk analytics dashboard.

---

## 📌 Project Overview

Banks and lending institutions need to understand borrower risk and portfolio performance to make better lending and risk-management decisions.

This project analyzes a large Lending Club loan dataset to answer questions such as:

* What is the overall loan default rate?
* How does default risk vary across FICO score ranges?
* Does higher DTI correspond to higher observed default rates?
* How does loan amount relate to default risk?
* Which loan purposes show higher observed default rates?
* How does borrower income relate to default patterns?
* Which states have higher observed default rates?
* How can borrowers be segmented into different risk groups?

---

## 🎯 Business Objectives

* Analyze overall loan portfolio performance
* Identify patterns associated with loan defaults
* Segment borrowers based on FICO score and DTI
* Analyze default rates across loan characteristics
* Perform state-level risk analysis
* Build an interactive Power BI dashboard for portfolio monitoring
* Demonstrate practical SQL and Python analytics skills

---

## 🗂️ Dataset

**Dataset:** Lending Club Loan Dataset

The dataset contains information related to:

* Loan amount
* Borrower annual income
* FICO score
* Debt-to-income ratio
* Employment length
* Loan purpose
* Home ownership
* State
* Loan issue date
* Default status

### Dataset Size

* **Records:** 1,347,681
* **Original columns:** 15
* **Final cleaned columns:** 13
* **Duplicate records:** 0
* **Overall observed default rate:** 19.98%

---

## 🛠️ Tools & Technologies

### Python

* Pandas
* NumPy
* Matplotlib

Used for:

* Data profiling
* Data quality checks
* Data cleaning
* Exploratory data analysis
* Risk analysis
* Feature engineering

### SQL

* MySQL
* MySQL Workbench

Used for:

* Portfolio-level analysis
* Aggregations
* CASE statements
* GROUP BY / HAVING
* Risk segmentation
* CTEs
* Window functions
* `DENSE_RANK()`

### Power BI

Used for:

* KPI cards
* Interactive slicers
* Risk analysis
* Portfolio segmentation
* State-wise analysis
* Interactive dashboard development

---

## 🧹 Data Cleaning

The dataset was checked for:

* Duplicate records
* Invalid loan amounts
* Invalid income values
* Invalid FICO scores
* Invalid DTI values
* Missing values

### Cleaning Actions

* Removed unnecessary text columns such as `title` and `desc`
* Replaced `dti_n = 999` with missing values because it represented an invalid/extreme placeholder
* Filled the single missing ZIP code with `Unknown`
* Retained valid loan records instead of deleting rows unnecessarily

### Final Dataset

**1,347,681 rows × 13 columns**

---

## 📊 Key Portfolio Metrics

| Metric               |     Value |
| -------------------- | --------: |
| Total Loans          | 1,347,681 |
| Total Loan Amount    |   $19.42B |
| Average Loan Amount  |   $14,408 |
| Total Defaults       |   269,249 |
| Overall Default Rate |    19.98% |

---

## 🔍 Risk Analysis

### FICO Score

Observed default rates increased as FICO score decreased:

| FICO Band | Default Rate |
| --------- | -----------: |
| Below 650 |       32.03% |
| 650–699   |       23.60% |
| 700–749   |       15.68% |
| 750+      |        8.88% |

---

### Debt-to-Income Ratio

Observed default rates increased across higher DTI bands:

| DTI Band | Default Rate |
| -------- | -----------: |
| 0–10     |       14.84% |
| 10–20    |       17.85% |
| 20–30    |       23.08% |
| 30–40    |       29.13% |
| 40+      |       ~30.7% |

---

### Loan Amount

Higher loan amount bands showed higher observed default rates:

| Loan Amount | Default Rate |
| ----------- | -----------: |
| 0–5K        |       15.81% |
| 5K–10K      |       17.24% |
| 10K–20K     |       21.58% |
| 20K–30K     |       22.95% |
| 30K–40K     |       24.48% |

---

### Annual Income

The analysis showed higher observed default rates among lower-income bands:

| Annual Income | Default Rate |
| ------------- | -----------: |
| Below 40K     |       ~23.6% |
| 40K–60K       |       ~21.7% |
| 60K–90K       |       ~19.9% |
| 90K–150K      |       ~17.0% |
| 150K+         |       ~15.1% |

---

## 🏷️ Loan Purpose Analysis

Default rates varied across different loan purposes.

Some of the observed higher-rate categories included:

* Small Business
* Renewable Energy
* Moving
* House
* Medical

Loan purpose was analyzed using SQL and visualized in Power BI.

---

## 🗺️ State-Level Analysis

State-level default rates were analyzed using a minimum threshold of **5,000 loans** to avoid highlighting states with very small sample sizes.

The analysis used:

```sql
HAVING COUNT(*) >= 5000
```

A SQL window function was then used to rank states by observed default rate:

```sql
DENSE_RANK() OVER (
    ORDER BY default_rate DESC
)
```

---

## 🎯 Risk Segmentation

Borrowers were segmented using **FICO score and DTI**:

* Lower Risk
* Moderate Risk
* High Risk
* Very High Risk

The segmentation was designed to identify combinations of lower credit scores and higher debt-to-income ratios associated with higher observed default rates.

---

## 📈 Power BI Dashboard

The interactive dashboard includes:

### KPI Cards

* Total Loans
* Total Loan Amount
* Average Loan Amount
* Default Rate

### Risk Analysis

* Default Rate by FICO Score
* Default Rate by DTI
* Default Rate by Loan Amount

### Portfolio Analysis

* Default Rate by Loan Purpose
* Top 10 States by Default Rate
* Loan Portfolio by Risk Segment

### Interactive Filters

* Issue Date
* Loan Purpose
* State

---

## 📁 Project Structure

```text
Bank_Loan_Risk_Profitability_Analytics/
│
├── data/
│   └── LC_loans_cleaned.csv
│
├── python/
│   ├── 01_data_profiling.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda_risk_analysis.py
│   └── 04_load_to_mysql.py
│
├── sql/
│   └── bank_loan_analysis.sql
│
├── powerbi/
│   └── Bank_Loan_Risk_Analytics.pbix
│
├── images/
│   └── dashboard.png
│
└── README.md
```

---

## 🚀 Project Workflow

```text
Raw Dataset
     ↓
Data Profiling
     ↓
Data Cleaning
     ↓
Python EDA & Risk Analysis
     ↓
MySQL Data Loading
     ↓
SQL Business Analysis
     ↓
Power BI Dashboard
     ↓
Risk & Portfolio Insights
```

---

## 💡 Key Insights

1. Lower FICO score bands showed substantially higher observed default rates.
2. Higher DTI bands were associated with higher observed default rates.
3. Larger loan amount bands showed higher observed default rates.
4. Lower annual-income bands showed higher observed default rates in this dataset.
5. Default rates varied meaningfully across loan purposes and states.
6. Combining FICO and DTI provides a useful framework for borrower risk segmentation.

> **Note:** These findings describe patterns observed in the analyzed dataset and should not be interpreted as causal relationships.

---

## 🔮 Future Improvements

Potential extensions of the project include:

* Predictive default-risk modeling
* Logistic regression / classification models
* Feature importance analysis
* Probability-of-default estimation
* Expected-loss modeling
* Time-based portfolio monitoring
* Automated Power BI refresh pipeline

---

## 👨‍💻 Author

**Ayush Pandey**

B.Sc. Information Technology
Data Analytics | Python | SQL | Power BI

---

## ⭐ Skills Demonstrated

**Python • Pandas • NumPy • Data Cleaning • EDA • MySQL • SQL • CTE • Window Functions • Power BI • Data Visualization • Risk Analytics • Business Analytics**
