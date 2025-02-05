# Compact Text Representation

The first way we can display estimators is through compact text representation. Estimators will only show the parameters that have been set to non-default values when displayed as a string. This reduces visual noise and makes it easier to spot the differences when comparing instances.

```python
from sklearn.linear_model import LogisticRegression

# Create an instance of Logistic Regression with l1 penalty
lr = LogisticRegression(penalty="l1")

# Display the estimator
print(lr)
```
