# Demographic Data Analyzer

This project analyzes demographic data extracted from the **1994 Census Database** using **Python and Pandas**.  
It is part of the **freeCodeCamp – Data Analysis with Python Certification**.

---

## 📌 Project Objective

The objective of this project is to analyze census data and answer questions related to:
- Age
- Education
- Income
- Working hours
- Race
- Country
- Occupation

The analysis is performed using **Pandas data manipulation and aggregation techniques**.

---

## 📊 Dataset Information

- Source: UCI Machine Learning Repository
- Dataset: Adult Census Income Dataset (1994)
- File used: `adult.data.csv`

Each row represents an individual with attributes such as age, education, occupation, working hours, country, and salary.

---

## 🛠️ Technologies Used

- Python 3.11
- Pandas
- VS Code
- Git & GitHub

---

## 📂 Project Structure

demographic-data-analyzer/
│
├── adult.data.csv
├── demographic_data_analyzer.py
├── main.py
└── README.md


---

## ⚙️ Function Description

### `calculate_demographic_data()`

This function computes the following:

1. Number of people of each race  
2. Average age of men  
3. Percentage of people with a Bachelor's degree  
4. Percentage of people with advanced education earning >50K  
5. Percentage of people without advanced education earning >50K  
6. Minimum number of hours worked per week  
7. Percentage of high earners among those working minimum hours  
8. Country with the highest percentage of people earning >50K  
9. Most popular occupation for high earners in India  

All percentage values are **rounded to one decimal place**.

---

## ▶️ How to Run the Project

Make sure you are using **Python 3.11**.

```bash
py -3.11 main.py

✅ Sample Output
Average age of men: 39.4
Percentage with Bachelors: 16.4
Higher education rich: 46.5
Lower education rich: 17.4
Highest earning country: Iran
Top occupation in India: Prof-specialty
