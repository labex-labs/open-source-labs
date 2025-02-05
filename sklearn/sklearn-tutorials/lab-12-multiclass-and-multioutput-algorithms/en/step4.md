# Multioutput Regression

#### Problem Description

Multioutput regression predicts multiple numerical properties for each sample. Each property is a numerical variable, and the number of properties can be greater than or equal to two.

#### Target Format

A valid representation of multioutput regression targets is a dense matrix, where each row represents a sample and each column represents a different property.

#### Example

Let's create a multioutput regression problem using the make_regression function:

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Generate a multioutput regression problem
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Fit a multioutput linear regression model
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```
