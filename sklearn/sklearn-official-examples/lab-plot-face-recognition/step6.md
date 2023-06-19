# Evaluate Model Performance

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

We predict the target values using the test data and evaluate the model performance using the `classification_report()` function. We also plot the confusion matrix using the `ConfusionMatrixDisplay()` function.


