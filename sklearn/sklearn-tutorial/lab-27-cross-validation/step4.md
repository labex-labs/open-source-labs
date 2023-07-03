# Train and evaluate the model

Now, let's train a support vector machine (SVM) classifier on the training set and evaluate its performance on the test set.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```

#
