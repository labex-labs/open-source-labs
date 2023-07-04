# Multiclass Classification

#### Problem Description

Multiclass classification is a classification task with more than two classes. Each sample is assigned to only one class.

#### Target Format

A valid representation of multiclass targets is a 1D or column vector containing more than two discrete values.

#### Example

Let's use the Iris dataset to demonstrate multiclass classification:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Fit a logistic regression model using OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```
