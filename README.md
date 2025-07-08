# 🏡 Real Estate Price Prediction with EDA & Ridge Regression

## 📌 Overview
This project explores house price prediction using housing data. 
While inspired by a YouTube tutorial, I personalized the project by enhancing the exploratory data analysis (EDA), adding regularized models (Ridge Regression), 
and visualizing prediction performance and residuals for deeper insights.

---

## 🔍 Key Enhancements

### 🧪 Exploratory Data Analysis (EDA)
- **Correlation Heatmap** to assess multicollinearity between variables (e.g., bedrooms and bathrooms highly correlated).
- **Boxplots**:
  - Price per square foot by bedroom count
  - Overall price distribution by bedroom count
- **Scatter Plot**:
  - Total square feet vs. Price, highlighting positive correlation and outliers

### 🤖 Modeling
- **Linear Regression** (Baseline)
- **Lasso Regression** (Comparison)
- **Decision Tree Regressor** (Comparison)
- **Ridge Regression** to mitigate multicollinearity and prevent overfitting

### 📊 Visual Diagnostics
- **Prediction vs Actual Plot**: Assessed how well the model generalizes
- **Residual Plot**: Evaluated error patterns and model bias

---

## 💡 Key Insights
- **Total square footage** showed a strong correlation with price.
- **Bedroom count and bathrooms** were highly correlated (0.90), prompting the use of Ridge Regression to address multicollinearity.
- Regularized Ridge model demonstrated better generalization, especially in outlier-prone segments.
- Visualizations made it easier to identify price anomalies and helped in business-focused storytelling.

---

## 🛠️ Technologies Used
- **Python**: Data analysis and modeling
- **Pandas**, **NumPy**: Data manipulation
- **Matplotlib**, **Seaborn**: Data visualization
- **Scikit-learn**: Regression modeling and metrics

---

## 📁 File Structure
- `Real_Estate_Price_Prediction_Project.ipynb`: Full notebook with step-by-step code, commentary, and visuals
- `Real_Estate_Data.csv`: Dataset used for this project (you can provide a dummy dataset or link to source)

---

## ✨ What I Learned
- How to make a tutorial project uniquely mine by customizing analysis and interpretation
- The importance of **residual analysis** and **model evaluation** beyond just metrics
- The power of **EDA in shaping model decisions** and **communicating findings**

---

## 🔗 View Project
- 📌 [Notebook on GitHub]([#](https://github.com/Esther-MM/Real_Estate_Project/blob/main/Model/Real_Estate_Price_Prediction_Project.ipynb))
- 🌐 [Portfolio Link](https://www.datascienceportfol.io/EstherMwangi)
- 💼 [Connect with me on LinkedIn]([#](http://linkedin.com/in/esther-mamtoshu-520595119))

---

## 👩🏾‍💻 Author
**Esther Mamtoshu**  
Senior Data Analyst | Data Scientist | Data Storyteller  
🔗 [LinkedIn](http://linkedin.com/in/esther-mamtoshu-520595119) | 🌐 [Portfolio](https://www.datascienceportfol.io/EstherMwangi)
