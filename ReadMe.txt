#  Student Performance Prediction & Analysis

##  Project Overview

This project demonstrates a complete beginner-friendly **Data Science and Machine Learning workflow** using a student performance dataset.

The project focuses on analyzing student performance, identifying relationships between different features, visualizing the data, building a machine learning model, and creating an interactive Power BI dashboard.

### The project includes:

-  Exploratory Data Analysis (EDA)
-  Data Visualization
-  Correlation and Outlier Analysis
-  Machine Learning using Linear Regression
-  Model Evaluation
-  Interactive Power BI Dashboard
-  GitHub Project Organization

---

##  Project Structure

```text
student-performance-project/
│
├── data/
│   └── PB_data.csv
│
├── notebooks/
│   └── analysis.py
│
├── powerbi/
│   └── Student_Performance_Dashboard.pbix
│
├── screenshots/
│   ├── boxplot.png
│   ├── heatmap.png
│   ├── histogram.png
│   └── powerbi_dashboard.png
│
├── README.md
└── requirements.txt

## Dataset

The dataset contains information related to student academic performance.
Dataset Features
Feature	Description
Hours	Number of study hours
Attendance	Student attendance percentage
PreviousMarks	Previous examination marks
Assignments	Assignment completion score
Marks	Final examination marks


The target variable for the machine learning model is Marks.

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed using Python libraries such as:
- Pandas
- NumPy
- Matplotlib
- Seaborn
EDA Steps
The following analysis was performed:
- Data loading and inspection
- Checking dataset shape
- Checking data types
- Missing value analysis
- Statistical summary
- Distribution analysis
- Correlation analysis
- Heatmap visualization
- Outlier detection using IQR
- Boxplot analysis
- Histogram visualization

## Data Visualizations

## Correlation Heatmap
The correlation heatmap was used to understand the relationships between numerical features in the dataset.
![Heatmap](screenshots/Heatmap.JPG)

## Boxplot — Outlier Analysis
Boxplots were used to analyze the distribution of the data and identify potential outliers.
![Boxplot](screenshots/BOXplot(outlier).JPG)

## Histogram
Histograms were used to understand the distribution of different features in the student performance dataset.
![Histogram](screenshots/Histogram.JPG)

## Machine Learning
## Model Used
Linear Regression
Linear Regression was used to predict students' final marks based on the available features.
Machine Learning Workflow

Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Prediction
   ↓
Model Evaluation

## Machine Learning Steps
The following steps were completed:
- Train/Test Split
- Model Training
- Prediction
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Cross Validation
- New Student Prediction

## Model Results
The Linear Regression model achieved the following results:
Metric	Result
R² Score	~0.9996
RMSE	~0.44
Cross Validation Average	~0.9948

These results indicate that the model performed very well on this dataset.
Note: Very high performance can sometimes indicate that the dataset has a strong linear relationship between the features and target variable. In real-world datasets, model performance should also be validated on unseen external data.

## Power BI Dashboard
An interactive Microsoft Power BI dashboard was created to visualize student performance and provide an easy-to-understand overview of the dataset.
Dashboard Includes
-  Average Marks Card
-  Bar Chart
-  Line Chart
-  Pie Chart
-  Interactive Slicers
-  Student Performance Table
-  Performance Analysis

## Power BI Dashboard Preview
![Power BI Dashboard](screenshots/PB_Dashboard.JPG)

Technologies Used
- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 🎨 Seaborn
- 🤖 Scikit-learn
- 📈 Microsoft Power BI
- 🐙 GitHub
▶️ How to Run
1. Clone the Repository
git clone https://github.com/hammeshkh5446-sudo/student-performance-project.git

2. Navigate to the Project Directory
cd student-performance-project

3. Install Required Libraries
pip install -r requirements.txt

4. Run the Analysis
python notebooks/analysis.py

5. Open the Power BI Dashboard
Open the following file using Microsoft Power BI Desktop:
powerbi/Student_Performance_Dashboard.pbix

## Learning Outcomes
Through this project, I gained practical experience in:

- Data loading and exploration
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Data visualization
- Correlation analysis
- Outlier detection
- Linear Regression
- Machine Learning fundamentals
- Model evaluation
- Cross-validation
- Making predictions
- Power BI dashboard development
- GitHub project organization

## Project Highlights
Python + Pandas
      ↓
Data Analysis & Cleaning
      ↓
Matplotlib + Seaborn
      ↓
Data Visualization
      ↓
Scikit-learn
      ↓
Machine Learning
      ↓
Linear Regression
      ↓
Model Evaluation
      ↓
Power BI
      ↓
Interactive Dashboard

## Project Screenshots

## Heatmap
![Heatmap](screenshots/Heatmap.JPG)

## Boxplot
![Boxplot](screenshots/BOXplot(outlier).JPG)

##  Histogram
![Histogram](screenshots/Histogram.JPG)

## Power BI Dashboard
![Power BI Dashboard](screenshots/PB_Dashboard.JPG)

## Author
M. Hammad Shahbaz
Computer Science / Software Engineering Student
GitHub: @HammadShahbaz911
