# Train Models

We will create two SVM models. The first model will not take into account sample weights, and the second model will take into account the sample weights we just created.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
