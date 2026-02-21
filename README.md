# 🚗 Car Price Predictor

A supervised machine learning project for predicting the resale value of used cars using regression techniques. The workflow covers data cleaning, feature transformation, and model training using **Pandas**, **NumPy**, and **Scikit-learn**.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## 📌 Overview

This project aims to predict the selling price of a used car based on features such as:

- Car brand and model
- Year of manufacture
- Kilometres driven
- Fuel type (Petrol / Diesel / CNG / Electric)
- Transmission type (Manual / Automatic)
- Number of previous owners
- Seller type (Dealer / Individual / Trustmark Dealer)

The model is trained using regression algorithms and evaluated with standard metrics such as R² score, MAE, and RMSE.

---

## 📂 Project Structure

```
Car-Price-Predictor/
│
├── data/                   # Raw and processed datasets
│   ├── raw/                # Original dataset files
│   └── processed/          # Cleaned and transformed data
│
├── notebooks/              # Jupyter notebooks for EDA and modelling
│
├── models/                 # Saved trained model files
│
├── src/                    # Source code modules
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── model.py
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore
```

> 📝 **Note:** This structure will expand as new files and modules are added to the project.

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computing |
| Scikit-learn | Machine learning models and evaluation |
| Matplotlib / Seaborn | Data visualisation |
| Jupyter Notebook | Exploratory data analysis |

---

## 📊 Dataset

<!-- Update this section once the dataset is added -->

The dataset contains information about used cars listed for sale. It includes features such as car name, year, selling price, present price, kilometres driven, fuel type, seller type, transmission, and owner history.

**Source:** *(Add dataset source/link here)*

**Columns:**

| Column | Description |
|---|---|
| `Car_Name` | Name of the car |
| `Year` | Year of purchase |
| `Selling_Price` | Price at which the car is being sold (target variable) |
| `Present_Price` | Current ex-showroom price |
| `Kms_Driven` | Distance driven in kilometres |
| `Fuel_Type` | Fuel type (Petrol / Diesel / CNG) |
| `Seller_Type` | Seller type (Dealer / Individual) |
| `Transmission` | Transmission type (Manual / Automatic) |
| `Owner` | Number of previous owners |

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aashi-25/Car-Price-Predictor.git
   cd Car-Price-Predictor
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

<!-- Update with actual notebook/script names once they are added -->

1. Place the dataset inside the `data/raw/` directory.
2. Open and run the Jupyter notebooks in the `notebooks/` folder in order:
   - `01_EDA.ipynb` – Exploratory Data Analysis
   - `02_Preprocessing.ipynb` – Data cleaning and feature engineering
   - `03_Model_Training.ipynb` – Model training and evaluation
3. Alternatively, run the end-to-end pipeline via:

   ```bash
   python src/model.py
   ```

---

## 🤖 Model Training

The following regression models are explored and compared:

- Linear Regression
- Ridge / Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

**Preprocessing steps include:**
- Handling missing values
- Encoding categorical variables (Label Encoding / One-Hot Encoding)
- Feature scaling (StandardScaler / MinMaxScaler)
- Feature selection based on correlation and importance scores

---

## 📈 Results

<!-- Update this section with actual metrics once training is complete -->

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | - | - | - |
| Random Forest | - | - | - |
| Gradient Boosting | - | - | - |

> ✅ Best performing model and final metrics will be updated here after experimentation.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes relevant comments.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

*Built with ❤️ by [Aashi-25](https://github.com/Aashi-25)*
