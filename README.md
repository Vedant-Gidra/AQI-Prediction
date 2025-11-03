# AQI Prediction and Web Deployment

## Problem Statement  
This project aims to **predict the Air Quality Index (AQI)** using various environmental and pollutant-based features such as **PM2.5, PM10, NO₂, SO₂, CO, and O₃** levels.  
Accurate AQI prediction helps identify pollution trends and supports decision-making in **air quality management**.  

Two machine learning models — **Random Forest Regressor** and **XGBoost Regressor** — were compared to determine the best performer.  
Based on performance and deployment simplicity, the **Random Forest model** was chosen for deployment via a **Flask web application**.

---

## Objective  
- Build machine learning models to predict AQI from given pollutant features.  
- Compare the performance of **XGBoost Regressor** and **Random Forest Regressor**.  
- Deploy the best-performing model (**Random Forest**) as a **web app** for real-time AQI prediction.  
- Enable users to input pollutant levels through a simple web interface and get instant AQI predictions.

---

## Approach  

### 1. Data Preprocessing  
- Handled **missing values** and **outliers**.  
- Cleaned and normalized the dataset for consistency.  
- Used pollutant concentrations as model input features and **AQI** as the target variable.  

### 2. Feature Engineering  
- Selected pollutant-based features:  
  - `PM2.5 (µg/m³)`  
  - `PM10 (µg/m³)`  
  - `NO₂ (ppb)`  
  - `SO₂ (ppb)`  
  - `CO (ppm)`  
  - `O₃ (ppb)`  
- Derived AQI as the prediction target.  

### 3. Model Training and Evaluation  
- Implemented both **Random Forest Regressor** and **XGBoost Regressor**.  
- Used **GridSearchCV** for hyperparameter tuning.  
- Split data into **training** and **testing** sets for validation.  
- Evaluated performance using **Mean Absolute Error (MAE)**.  

### 4. Model Deployment  
- Saved the trained Random Forest model using **Pickle**.  
- Built a **Flask backend** to handle model inference.  
- Created a **simple HTML frontend** to take pollutant inputs and display the predicted AQI.  

---

## Results
<img width="754" height="266" alt="image" src="https://github.com/user-attachments/assets/a131c70e-787e-404a-9085-47a878c81dcf" />

- Both **XGBoost** and **Random Forest** achieved similar prediction accuracy with a **Mean Absolute Error (MAE)** of **0.0285**.  
- However, **Random Forest** was chosen for deployment because:  
  - It is **faster to train** on medium-sized datasets.  
  - **Easier to interpret** and debug.  
  - **Requires fewer dependencies** and is simpler to deploy.  
  - Provides **comparable accuracy** to XGBoost for this dataset.  

---

## Technologies Used  
- **Python**  
- **Flask** (for web deployment)  
- **Scikit-learn**  
- **XGBoost**  
- **Pandas / NumPy / Matplotlib / Seaborn**  
- **HTML / CSS** (for frontend)  
- **Jupyter Notebook**

---

## Dataset  
**Source:** [India Air Quality Dataset (Delhi)](https://github.com/cp099/India-Air-Quality-Dataset/blob/main/Delhi_AQI_Dataset.csv)  

**Columns Description:**
| Column | Description |
|--------|-------------|
| City | Name of the city |
| Date | Date of recorded AQI |
| AQI | Air Quality Index (as per CPCB) |
| PM2.5 | Fine Particulate Matter (µg/m³) |
| PM10 | Coarse Particulate Matter (µg/m³) |
| NO₂ | Nitrogen Dioxide (ppb) |
| SO₂ | Sulfur Dioxide (ppb) |
| CO | Carbon Monoxide (ppm) |
| O₃ | Ozone (ppb) |

---

## How It Works  

### 🔹 Application Flow
1. The user opens the web app (`/` endpoint) which displays the input form.  
2. User enters pollutant levels:  
   - PM2.5 (µg/m³)  
   - PM10 (µg/m³)  
   - NO₂ (ppb)  
   - SO₂ (ppb)  
   - CO (ppm)  
   - O₃ (ppb)  
3. On submitting the form, a POST request is sent to the **`/predict`** endpoint.  
4. Flask backend retrieves the input values, processes them into a feature vector, and passes them to the trained **Random Forest model**.  
5. The model predicts the **Air Quality Index (AQI)**.  
6. The result is rendered back to the user on the same page.

### 🔹 API Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Displays the web interface for AQI prediction. |
| `/predict` | POST | Accepts pollutant input values and returns the predicted AQI. |

---

## 🏁 Future Improvements  
- Add **real-time AQI data visualization**.  
- Integrate **API-based city-wise prediction**.  
- Include **AQI category and health recommendations** in output.  
- Deploy on **Render / Heroku / AWS** for public access.

---

## 📸 Sample Interface  
<img width="727" height="710" alt="image" src="https://github.com/user-attachments/assets/399e9496-8d68-4ca7-beca-a00394bcc68c" />



---

## 👨‍💻 Author  
**Vedant Gidra**  
B.Tech in Software Engineering  
