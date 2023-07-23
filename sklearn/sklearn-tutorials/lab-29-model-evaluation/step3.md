# Metric Functions

The scikit-learn `metrics` module implements several functions for assessing prediction error for specific purposes. These functions can be used to calculate the quality of predictions made by a model.

Here's an example of using the `accuracy_score` function from the `metrics` module:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
