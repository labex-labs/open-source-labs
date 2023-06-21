# Train the Model

In this step, we will train the SVM classifier with RBF kernel using the generated data.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
