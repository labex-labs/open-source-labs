# Estimator Score Method

The Estimator score method is a default evaluation criterion provided by scikit-learn for each estimator. It calculates a score that represents the quality of the model's predictions. You can find more information about this in the documentation of each estimator.

Here's an example of using the `score` method for an estimator:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()
clf.fit(X, y)

score = clf.score(X, y)
print("Score:", score)
```
