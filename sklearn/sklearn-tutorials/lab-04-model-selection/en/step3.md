# Grid-Search

Grid-search is a technique that can be used to find the best combination of parameter values for an estimator. It involves specifying a grid of parameter values, fitting the estimator on the training data for each combination of parameters, and selecting the parameters that result in the highest cross-validation score.

```python
from sklearn.model_selection import GridSearchCV

# Define a grid of parameter values
Cs = np.logspace(-6, -1, 10)

# Create a GridSearchCV object with the SVM classifier and the parameter grid
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Fit the GridSearchCV object on the training data
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
