# Calculate the OOB Error Rate

For each classifier, we will loop through a range of `n_estimators` values and fit the classifier to the dataset. We will record the OOB error rate for each `n_estimators` value and store it in an `OrderedDict` object.

```python
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

min_estimators = 15
max_estimators = 150

for label, clf in ensemble_clfs:
    for i in range(min_estimators, max_estimators + 1, 5):
        clf.set_params(n_estimators=i)
        clf.fit(X, y)

        oob_error = 1 - clf.oob_score_
        error_rate[label].append((i, oob_error))
```
