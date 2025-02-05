# Train Model

We will train a support vector machine (SVM) classifier using a linear kernel. We will use a regularization parameter C that is too low to see the impact on the results.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
