# Cross-Validation Generators

Scikit-learn provides a collection of classes that can be used to generate train/test indices for popular cross-validation strategies. These classes have a `split` method that accepts the input dataset and yields the train/test set indices for each iteration of the cross-validation process.

```python
from sklearn.model_selection import KFold

# Split the data into K folds using KFold cross-validation
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

The `cross_val_score` helper function can be used to calculate the cross-validation score directly. It splits the data into training and test sets for each iteration of cross-validation, trains the estimator on the training set, and computes the score based on the test set.

```python
from sklearn.model_selection import cross_val_score

# Calculate the cross-validation score for the SVM classifier
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
