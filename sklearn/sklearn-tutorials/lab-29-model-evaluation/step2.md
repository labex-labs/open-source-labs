# Scoring Parameter

Scikit-learn provides a `scoring` parameter in several model evaluation tools, such as cross-validation and grid search. The `scoring` parameter controls the metric applied to the estimators during evaluation.

Here's an example of using the `scoring` parameter with cross-validation:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
clf = LogisticRegression()

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print("Scores:", scores)
```
