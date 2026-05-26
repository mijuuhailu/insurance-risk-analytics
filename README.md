# Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on historical auto insurance data from AlphaCare Insurance Solutions (ACIS) in South Africa. The goal is to identify low-risk customer segments, understand claim behavior, and support data-driven pricing and marketing strategies.

The analysis uses historical insurance data covering approximately 18 months (Feb 2014 – Aug 2015).

---

# Business Objective

AlphaCare Insurance Solutions (ACIS) aims to:

- Optimize insurance pricing strategies
- Identify profitable customer segments
- Improve marketing targeting
- Reduce underwriting risk
- Move toward analytics-driven decision making

This project explores claim patterns, profitability, and risk drivers using descriptive analytics and visualization techniques.

---

# Dataset Description

The dataset contains information related to:

## Policy Information
- UnderwrittenCoverID
- PolicyID

## Client Information
- Gender
- MaritalStatus
- Citizenship
- Language
- Bank
- AccountType

## Vehicle Information
- VehicleType
- make
- Model
- RegistrationYear
- kilowatts
- cubiccapacity
- CustomValueEstimate

## Geographic Information
- Province
- PostalCode
- MainCrestaZone
- SubCrestaZone

## Insurance Plan Information
- CoverType
- CoverCategory
- Product
- SumInsured
- CalculatedPremiumPerTerm

## Financial Information
- TotalPremium
- TotalClaims

---

# Derived Business Metrics

Two important insurance profitability metrics were created:

## Loss Ratio

Loss Ratio = TotalClaims / TotalPremium

This measures portfolio profitability.

- Loss Ratio < 1 → profitable
- Loss Ratio > 1 → unprofitable

## Margin

Margin = TotalPremium − TotalClaims

This measures profit contribution per policy.

---

# Exploratory Data Analysis (EDA)

The following analyses were performed:

## 1. Data Summarization
- Dataset shape inspection
- Data type validation
- Descriptive statistics for numerical variables

## 2. Data Quality Assessment
- Missing value analysis
- Duplicate checks
- Date conversion and formatting

## 3. Univariate Analysis
- Histograms for financial variables
- Distribution analysis
- Bar charts for categorical features

## 4. Bivariate & Multivariate Analysis
- Correlation matrix
- Premium vs Claims scatter plots
- Loss Ratio comparisons across categories

## 5. Geographic Analysis
- Province-level risk comparison
- Regional profitability trends

## 6. Outlier Detection
- Boxplots for:
  - TotalClaims
  - TotalPremium
  - CustomValueEstimate
  - LossRatio

## 7. Temporal Trend Analysis
- Monthly Loss Ratio trends
- Claim frequency patterns over time

---

# Key Findings

## Portfolio Profitability
- Overall portfolio Loss Ratio: **1.048**
- The insurer pays approximately R1.05 in claims for every R1.00 collected in premiums.
- This suggests the portfolio is slightly unprofitable overall.

## Geographic Risk
- Gauteng showed the highest Loss Ratio.
- Northern Cape showed the lowest Loss Ratio.
- Significant regional differences in risk exposure were observed.

## Temporal Trends
- Monthly Loss Ratios fluctuated substantially over time.
- Certain periods experienced unusually high claim severity.

## Correlation Insights
- TotalClaims and LossRatio showed moderate positive correlation.
- Margin had a strong negative relationship with claims.
- Premiums alone did not strongly predict claims.

## Outliers
- Financial variables were heavily right-skewed.
- Extreme claim values and vehicle values were identified.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# Visualizations Created

The project includes:
- Loss Ratio by Province
- Monthly Loss Ratio Trend
- Correlation Heatmap
- Boxplots for Outlier Detection
- Premium vs Claims Scatter Plot
- Vehicle Risk Comparisons
