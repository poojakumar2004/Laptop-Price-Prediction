# Laptop Price Prediction Using Machine Learning

## 📌 Project Title

**Laptop Price Prediction Using Machine Learning**

## 📖 Project Description

Laptop Price Prediction is a machine learning project that predicts the price of a laptop based on its specifications. The system analyzes various hardware and software features such as processor type, RAM, storage, graphics card, operating system, screen size, and brand to estimate the laptop's market price.

This project helps users compare laptop configurations and provides an estimated price based on historical data and machine learning models.

---

## 🎯 Objectives

* Predict laptop prices using machine learning algorithms.
* Analyze the impact of different laptop specifications on price.
* Improve decision-making for buyers and sellers.
* Provide accurate price estimates through a simple interface.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Flask (for web application)

---

## 📂 Dataset Features

The dataset includes the following laptop specifications:

* Brand/Company
* Laptop Type
* Processor (CPU)
* RAM
* Storage (HDD/SSD)
* Graphics Card (GPU)
* Operating System
* Screen Size
* Weight
* Screen Resolution
* Price (Target Variable)

---

## 🔄 Project Workflow

### Data Collection

Laptop specification data is collected from publicly available sources.

### Data Preprocessing

* Removing missing values
* Handling categorical data
* Feature engineering
* Data cleaning

### Exploratory Data Analysis (EDA)

* Understanding data distribution
* Identifying important features
* Visualizing relationships between features and price

### Model Training

Different regression algorithms are used to train the model:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### Model Evaluation

Performance is evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

### Prediction

The trained model predicts the laptop price based on user-provided specifications.

---

## 📊 Sample Input

| Feature     | Value            |
| ----------- | ---------------- |
| Brand       | HP               |
| Processor   | Intel Core i5    |
| RAM         | 8 GB             |
| Storage     | 512 GB SSD       |
| GPU         | Intel Integrated |
| Screen Size | 15.6 inch        |

### Sample Output

```text
Predicted Laptop Price: ₹58,000
```

---

## 📈 Results

The machine learning model successfully predicts laptop prices with good accuracy. Features such as processor type, RAM, storage capacity, and graphics card have the greatest influence on the predicted price.

---

## 🔮 Future Enhancements

* Real-time laptop price updates
* Cloud deployment
* Mobile application support
* Advanced machine learning models for higher accuracy

---

## 👨‍💻 Author

**Github**- https://github.com/poojakumar2004/

---

## 📜 License

This project is intended for educational and academic purposes only.
