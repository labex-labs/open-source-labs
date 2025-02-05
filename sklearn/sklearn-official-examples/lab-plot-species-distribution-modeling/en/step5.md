# Fit OneClassSVM

In this step, we will fit the OneClassSVM model to the training data. We will standardize the features and fit the OneClassSVM model to the training data.

```python
# Standardize features
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# Fit OneClassSVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
