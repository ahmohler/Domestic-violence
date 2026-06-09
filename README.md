# Domestic Violence Prediction

A simple data science project that utilizes machine learning to analyze and predict the likelihood of domestic violence based on basic demographic and socioeconomic factors.

## Features
- **Data Cleaning**: Basic preprocessing of demographic records.
- **Data Visualization**: Age distribution analysis across violence cases.
- **Predictive Model**: A Random Forest Classifier to predict violence occurrence.

## Dataset Features
The model utilizes a small dataset containing the following attributes:
- `Age`: Age of the individual.
- `Income` / `Employment` / `Education`: Socioeconomic status indicators.
- `Marital status`: Marital state (Married / Unmarried).
- `Violence`: The target variable (Yes / No).

## How to Run
1. Install dependencies: 
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
