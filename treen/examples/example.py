import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from treen.lightgbm import LightGBMPredictor  # Assuming this is the correct import

# 1. Load dataset (Boston Housing dataset)
from sklearn.datasets import fetch_california_housing

# Load California housing dataset
data = fetch_california_housing()
X, y = pd.DataFrame(data.data, columns=data.feature_names), data.target



# 2. Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize the LightGBMPredictor model from treen
model = LightGBMPredictor(params={'objective': 'regression', 'metric': 'rmse'})

# 4. Fit the model
model.fit(X_train, y_train)

# 5. Make predictions on the test set
y_pred = model.predict(X_test)

# 6. Evaluate the predictions
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# 7. Plot true vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2)  # Line of perfect prediction
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
plt.title("True vs. Predicted Values")
plt.grid(True)
plt.show()
