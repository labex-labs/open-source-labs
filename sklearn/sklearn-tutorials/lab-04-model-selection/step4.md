# Cross-Validated Estimators

Some estimators in scikit-learn have built-in cross-validation capabilities. These cross-validated estimators automatically select their parameters by cross-validation, making the model selection process more efficient.

```python
from sklearn import linear_model, datasets

# Create a LassoCV object
lasso = linear_model.LassoCV()

# Load the diabetes dataset
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Fit the LassoCV object on the dataset
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
