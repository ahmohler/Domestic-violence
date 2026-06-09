# Domestic Violence Prediction & Analysis

A data science project that combines machine learning and spreadsheet analysis to investigate and predict the likelihood of domestic violence based on demographic and socioeconomic factors.

## Features
- **Data Preprocessing**: String trimming, handling target variable encoding (Yes/No to 1/0).
- **Hybrid Analysis Approach**: 
  - **Python (Machine Learning)**: Feature engineering and predictive modeling.
  - **Excel (Statistical Analysis)**: Pivot tables and dynamic cross-tabulation.
- **Data Visualization**: Stacked distribution charts linking age cohorts with violence occurrence.

## Dataset Attributes
The analysis is performed on a dataset containing the following attributes:
- `Age`: Age of the individual.
- `Income` / `Employment` / `Education`: Socioeconomic status indicators.
- `Marital Status`: Marital state (Married / Unmarried).
- `Violence` / `Violence_Numeric`: The target indicator (Yes = 1, No = 0).

---

## 📊 Data Visualization & Insights
Below is the stacked distribution chart generated through Excel PivotTables, highlighting how violence cases are distributed across different age cohorts:

![Violence Age Distribution](violence_age_distribution.png)

---

## 🛠️ How to Run the Python Model

### 1. Install Dependencies
Ensure you have the required libraries installed:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn

2. Execute the Predictive Script
Run the machine learning pipeline (Random Forest Classifier) using the following command:
python3 model.py

3. Model Performance Evaluation
The Random Forest model yields an overall accuracy of 71% upon evaluation against the unseen test partition:

           0       0.80      0.83      0.81        53
           1       0.40      0.35      0.38        17

    accuracy                           0.71        70
   macro avg       0.60      0.59      0.59        70
weighted avg       0.70      0.71      0.71        70
