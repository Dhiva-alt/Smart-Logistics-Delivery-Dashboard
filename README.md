# Smart Logistics Delivery Dashboard

## Project Overview

The Smart Logistics Delivery Dashboard is a data analytics and machine learning project developed to analyze food delivery operations and predict delivery times using historical logistics data.

This project combines:
- SQL for data analysis
- Python for machine learning prediction
- Power BI for interactive dashboards

The dashboard helps understand:
- Delivery performance
- Traffic impact
- Vehicle efficiency
- Weather influence
- Delivery time prediction

---

# Objectives

The main objectives of this project are:

- Analyze delivery operations using data analytics
- Identify factors affecting delivery time
- Compare vehicle performance
- Study route and traffic impact
- Predict delivery time using Machine Learning
- Create interactive dashboards for visualization

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data preprocessing & ML model |
| Pandas | Data analysis |
| Scikit-learn | Machine learning |
| MySQL | Data storage & SQL analysis |
| Power BI | Dashboard visualization |
| VS Code | Python development |
| MySQL Workbench | SQL queries and database management |

---

# Dataset Information

Dataset Name:
Food_Delivery_Times.csv

Dataset contains:
- Order ID
- Distance
- Weather
- Traffic Level
- Time of Day
- Vehicle Type
- Preparation Time
- Courier Experience
- Delivery Time

Total Records:
1000 Rows

---

# Database Creation

## Database Name

```sql
CREATE DATABASE smart_logistics_db;
```

## Table Creation

```sql
CREATE TABLE delivery_data (
    Order_ID INT PRIMARY KEY,
    Distance_km DECIMAL(5,2),
    Weather VARCHAR(20),
    Traffic_Level VARCHAR(20),
    Time_of_Day VARCHAR(20),
    Vehicle_Type VARCHAR(20),
    Preparation_Time_min INT,
    Courier_Experience_yrs INT,
    Delivery_Time_min INT
);
```

---

# SQL Analysis Performed

## Average Delivery Time

```sql
SELECT AVG(Delivery_Time_min)
FROM delivery_data;
```

## Orders by Weather

```sql
SELECT Weather, COUNT(*) AS Total_Orders
FROM delivery_data
GROUP BY Weather;
```

## Vehicle Wise Average Delivery Time

```sql
SELECT Vehicle_Type,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Vehicle_Type;
```

## Traffic Level Analysis

```sql
SELECT Traffic_Level,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Traffic_Level;
```

## Time of Day Analysis

```sql
SELECT Time_of_Day,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Time_of_Day;
```

---

# Additional SQL Feature

A new column called Delivery_Status was added to categorize deliveries.

## Query Used

```sql
ALTER TABLE delivery_data
ADD Delivery_Status VARCHAR(20);
```

```sql
UPDATE delivery_data
SET Delivery_Status =
CASE
    WHEN Delivery_Time_min > 60 THEN 'Delayed'
    WHEN Delivery_Time_min BETWEEN 40 AND 60 THEN 'On Time'
    ELSE 'Fast'
END;
```

---

# Python Machine Learning Model

## Model Used

Linear Regression

## Python Libraries Used

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
```

---

# ML Workflow

1. Load Dataset
2. Handle Missing Values
3. Encode Categorical Data
4. Train-Test Split
5. Train Linear Regression Model
6. Predict Delivery Time
7. Evaluate Model Performance

---

# Model Performance

| Metric | Value |
|---|---|
| Model | Linear Regression |
| Mean Absolute Error (MAE) | 7.26 |
| Dataset Size | 1000 |
| Prediction Accuracy | Moderate Accuracy |

---

# Power BI Dashboards

## 1. Overview Dashboard

Contains:
- Avg Delivery Time
- Avg Courier Experience
- Total Orders
- Avg Distance
- Vehicle Analysis
- Weather Analysis
- Time of Day Analysis

---

## 2. Route Analysis Dashboard

Contains:
- Traffic Level Analysis
- Distance vs Delivery Time
- Route Insights
- Weather Impact

---

## 3. Vehicle Performance Dashboard

Contains:
- Best Vehicle Analysis
- Avg Delivery Time by Vehicle
- Vehicle Usage Distribution
- Courier Experience Comparison

---

## 4. Prediction Dashboard

Contains:
- MAE KPI
- Model Information
- Dataset Size
- Accuracy Indicator
- Actual vs Predicted Delivery Time Scatter Plot
- Trend Line Visualization

---

# Key Insights

- High traffic increases delivery time significantly
- Bikes perform better for faster delivery
- Weather conditions affect delivery efficiency
- Longer distances increase delivery time
- Courier experience slightly improves delivery performance
- Linear Regression model predicts delivery time reasonably well

---

# Project Outcomes

This project successfully demonstrates:
- Data Cleaning
- SQL Analysis
- Dashboard Design
- Machine Learning Prediction
- Business Intelligence Reporting

---

# Future Improvements

Possible future enhancements:
- Real-time delivery tracking
- Advanced ML models
- Interactive filters
- Live database integration
- API-based prediction system

---

# Screenshots

## Overview Dashboard
![Overview Dashboard](<img width="1423" height="745" alt="Screenshot 2026-05-10 221206" src="https://github.com/user-attachments/assets/d3019653-6bd4-43fd-b540-5832c484954c" />
)


## Route Analysis Dashboard
![Route Analysis Dashboard](<img width="1389" height="760" alt="Screenshot 2026-05-10 221232" src="https://github.com/user-attachments/assets/9b82abfb-d905-45bf-83b3-f58f6498a7fc" />
)

## Vehicle Performance Dashboard
![Vehicle Performance Dashboard](<img width="1387" height="738" alt="Screenshot 2026-05-11 170551" src="https://github.com/user-attachments/assets/eef1ba49-20c9-4354-ad87-d16c9640a1d6" />
)

## Prediction Dashboard
![Prediction Dashboard](<img width="1382" height="749" alt="Screenshot 2026-05-10 221319" src="https://github.com/user-attachments/assets/817eb66a-7250-412d-96c3-997a0c21decf" />
)

---

# Conclusion

The Smart Logistics Delivery Dashboard project provides a complete analytics solution for delivery operations using SQL, Python, Machine Learning, and Power BI.

The project helps businesses:
- monitor delivery efficiency,
- understand operational patterns,
- and predict future delivery times effectively.

---

# Author

Dhivashini R

---

# GitHub Repository Name

Smart-Logistics-Delivery-Dashboard
