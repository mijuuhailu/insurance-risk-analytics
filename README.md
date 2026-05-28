# End-to-End Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project focuses on insurance risk analytics and predictive modeling using historical auto insurance data from South Africa. The objective is to identify low-risk customer segments, evaluate portfolio profitability, and develop machine learning models that support risk-based pricing strategies.

The project simulates a real-world insurance analytics workflow, including:

- Exploratory Data Analysis (EDA)
- Data Version Control (DVC)
- Statistical Hypothesis Testing
- Predictive Modeling
- Model Explainability using SHAP

---

# Business Problem

AlphaCare Insurance Solutions (ACIS) aims to optimize its pricing strategy and marketing investments by leveraging historical claims data.

The company wants to:
- Identify profitable low-risk customers
- Improve underwriting decisions
- Detect geographic and demographic risk patterns
- Build predictive pricing models
- Move toward data-driven insurance pricing

---

# Dataset Description

The dataset contains approximately 18 months of historical insurance data (Feb 2014 – Aug 2015).

## Key Data Categories

### Policy Information
- UnderwrittenCoverID
- PolicyID

### Client Information
- Gender
- MaritalStatus
- Language
- Citizenship

### Geographic Information
- Province
- PostalCode
- MainCrestaZone

### Vehicle Information
- VehicleType
- make
- Model
- RegistrationYear
- kilowatts
- CustomValueEstimate

### Insurance Plan Information
- CoverType
- Product
- SumInsured
- CalculatedPremiumPerTerm

### Financial Information
- TotalPremium
- TotalClaims

---

# Business Metrics

## Loss Ratio

Loss Ratio measures portfolio profitability.

```math
LossRatio = TotalClaims / TotalPremium
```

- Loss Ratio < 1 → profitable
- Loss Ratio > 1 → unprofitable

## Margin

```math
Margin = TotalPremium - TotalClaims
```

This represents profit contribution per policy.

---

# Project Tasks

## Task 1 — Exploratory Data Analysis (EDA)

Performed:
- Data summarization
- Missing value analysis
- Univariate analysis
- Correlation analysis
- Geographic trend analysis
- Outlier detection
- Temporal trend analysis

### Key Findings
- Portfolio Loss Ratio = 1.048
- The portfolio was slightly unprofitable overall
- Significant claim volatility existed over time
- Gender showed statistically significant claim differences
- Financial variables exhibited heavy right-skew and outliers

---

## Task 2 — Data Version Control (DVC)

Implemented DVC to ensure:
- Reproducibility
- Dataset versioning
- Auditability

### DVC Workflow
- Initialized DVC
- Configured local remote storage
- Tracked raw and cleaned datasets
- Versioned datasets using `.dvc` files

---

## Task 3 — A/B Hypothesis Testing

Performed statistical testing on:
- Province risk differences
- Zip code risk differences
- Gender risk differences

### Statistical Tests Used
- T-Test
- Chi-Square Test

### Key Results

| Hypothesis | P-Value | Decision |
|---|---|---|
| Province Risk Difference | 0.062 | Fail to Reject H₀ |
| Zip Code Risk Difference | 0.546 | Fail to Reject H₀ |
| Gender Risk Difference | 0.004 | Reject H₀ |

### Business Insight
Gender demonstrated statistically significant differences in insurance risk behavior.

---

## Task 4 — Statistical Modeling & Risk-Based Pricing

Built predictive models for claim severity estimation.

### Models Implemented
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

### Evaluation Metrics
- RMSE
- R² Score

### Feature Engineering
- VehicleAge
- LossRatio
- Claim Indicator

### Explainability
Used SHAP analysis to identify the most influential features affecting claim predictions.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- DVC
- Git & GitHub
- Jupyter Notebook

---

# Project Structure

```text
insurance-risk-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── eda.ipynb
│   ├── hypothesis_testing.ipynb
│   └── modeling.ipynb
│
├── src/
│   ├── hypothesis_tests.py
│   └── modeling.py
│
├── .dvc/
├── README.md
└── requirements.txt
```

---

# Future Improvements

Potential next steps include:
- Hyperparameter tuning
- Advanced feature engineering
- Fraud detection models
- Deep learning approaches
- Real-time pricing systems
- Deployment using FastAPI or Streamlit

---

