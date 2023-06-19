# Create SVM Classifier

In this step, we will create an instance of SVM classifier and fit our data. We will use the custom kernel created in the previous step.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```


