# train_iris.py
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib  # to save the model

# 1. Load dataset (small, clean, great for beginners)
iris = datasets.load_iris()
X = iris.data      # features (sepal/petal lengths & widths)
y = iris.target    # labels (0,1,2 for species)

# 2. Split into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Optional: scale features (helps some models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Choose model: Random Forest (robust & easy)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 5. Train (fit) on training data
model.fit(X_train_scaled, y_train)

# 6. Evaluate on test data
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print("Test accuracy:", acc)
print("\nClassification report:\n", classification_report(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

# 7. Quick cross-validation on the whole dataset (optional sanity check)
scores = cross_val_score(model, scaler.transform(X), y, cv=5)
print("5-fold CV accuracy (approx):", scores.mean())

# 8. Save the scaler + model for later use
joblib.dump(scaler, "iris_scaler.joblib")
joblib.dump(model, "iris_rf_model.joblib")
print("Saved model and scaler to disk.")
