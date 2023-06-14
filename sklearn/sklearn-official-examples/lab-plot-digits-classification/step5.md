# Train the Support Vector Machine

We will train a support vector classifier on the train samples using `svm.SVC()` method from `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```


