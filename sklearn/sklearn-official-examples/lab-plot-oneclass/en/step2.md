# Fit the one-class SVM model

Next, we will fit the one-class SVM model on the generated data.

```python
# Fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Predict the labels for the training data, regular novel observations, and abnormal novel observations
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
