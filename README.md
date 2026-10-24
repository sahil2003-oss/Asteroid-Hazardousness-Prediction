# Impact Watch - Asteroid Hazardousness Prediction

A high-performance machine learning classifier and web application designed to categorize and predict the hazardousness of asteroids based on astronomical parameters.

---

## Overview

Dealing with a heavily imbalanced asteroid hazard dataset from Kaggle, this project covers advanced data profiling, multicollinearity reduction, class-imbalance management, and deployment behind a fast, modern API backend.

---

## Key Features

* Advanced Exploratory Analysis: Generated full EDA reports using `ydata-profiling` to surface outliers, multicollinearity, and overlapping feature distributions across classes.
* Data Hygiene: Eliminated redundant features to resolve perfect multicollinearity and applied stratified train-test splitting with stratified k-fold cross-validation.
* Class-Imbalance Optimization: Trained and compared multiple classifiers (Random Forest, Decision Tree, XGBoost, AdaBoost, Gradient Boosting), optimizing specifically for **recall** to minimize false negatives on hazardous objects.
* Production Results: Selected a top-performing Random Forest classifier achieving **0.9801 recall** on the test set.
* Full-Stack Integration: Deployed behind a **FastAPI** backend coupled with a custom interactive frontend.

---

## Tech Stack

* **Language**: Python
* **ML Frameworks & Libraries**: scikit-learn, Numpy, Pandas, ydata-profiling
* **Backend**: FastAPI
* **Deployment**: Render

---

## Getting Started

### Prerequisites

* Python 3.x

### Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/sahil2003-oss/impact-watch-asteroid-hazardousness.git](https://github.com/sahil2003-oss/impact-watch-asteroid-hazardousness.git)
   cd impact-watch-asteroid-hazardousness

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Backend API**:
   ```bash
   uvicorn main:app --reload

4. **Open index.html file**:
   * Simple Open it by double click
