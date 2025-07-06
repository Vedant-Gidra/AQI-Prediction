# AQI Prediction

## Problem Statement

This project aims to **predict the Air Quality Index (AQI)** using various environmental and pollutant-based features such as levels of PM2.5, PM10, NO2, SO2, CO, and O3. Accurately forecasting AQI values can help in identifying pollution trends and aiding decision-makers in air quality management.

## Objective

- Build machine learning models to predict AQI from given features.
- Compare the performance of **XGBoost Regressor** and **Random Forest Regressor**.
- Analyze which model provides more accurate results and assess if one significantly outperforms the other.

## Approach

1. **Data Preprocessing**:
   - Handled missing values and outliers.
   - Normalized and cleaned the dataset for consistency.
2. **Feature Engineering**:
   - Used pollutant concentrations as input features.
   - Derived AQI as the target variable.
3. **Model Training**:
   - Implemented **Random Forest Regressor** and **XGBoost Regressor**.
   - Used train-test split to validate performance.
4. **Model Evaluation**:
   - Used metrics like **Mean Absolute Error (MAE)** and **R² Score** to evaluate models.
   - Compared results from both algorithms.

## Results
![image](https://github.com/user-attachments/assets/31488a7d-dc98-4e74-ba17-c6311f1a6689)
![image](https://github.com/user-attachments/assets/c65a435a-64a7-4e5d-a76b-50800dbcd79f)
![image](https://github.com/user-attachments/assets/070fdbe1-e230-46b7-bc24-97558769ed8d)

- Both **XGBoost** and **Random Forest** produced **similar results** in terms of prediction accuracy.
- The performance metrics showed only marginal differences, indicating both models are suitable for AQI prediction with this dataset.

## Technologies Used

- Python
- Scikit-learn
- XGBoost
- Pandas / NumPy / Matplotlib / Seaborn
- Jupyter Notebook

