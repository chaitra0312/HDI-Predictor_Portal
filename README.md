# A Comprehensive Measure of Well-Being: HDI Predictor Portal

An Artificial Intelligence & Machine Learning web application that utilizes data science metrics to predict a country's Human Development Index (HDI) value and matches it to its corresponding United Nations Development Programme (UNDP) operational classification tier.

## Tech Stack & Core Libraries
* **Language:** Python
* **Web Architecture Framework:** Flask (WSGI Engine)
* **Data Engineering / Analysis:** Pandas, NumPy
* **Machine Learning Algorithm:** Scikit-Learn (Linear Regression Engine)
* **Visualization Modules:** Matplotlib, Seaborn

##  Model Performance Analytics
* **Mean Squared Error (MSE):** 0.00291
* **R-squared ($R^2$) Score:** 0.85523 (Explains 85.5% of variance)

##  Repository Layout Directory
* models : Contains the serialized `hdi_model.pkl` weights tracking array.
* templates : Holds `index.html` structure forms.
* app.py : Core Flask microserver application backend controller file.
* notebook.ipynb : Google Colab model training and exploration logic workflow history.
