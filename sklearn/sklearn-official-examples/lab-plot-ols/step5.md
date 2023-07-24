# Calculate Metrics

We can calculate the coefficients, mean squared error, and coefficient of determination.

```python
from sklearn.metrics import mean_squared_error, r2_score

# The coefficients
print("Coefficients: \n", regr.coef_)

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
