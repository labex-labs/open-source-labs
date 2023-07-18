# Predict and Evaluate the Model

We will use the trained model to predict the value of the digits for the samples in the test subset. Then, we will evaluate the model using `metrics.classification_report()` and `metrics.ConfusionMatrixDisplay.from_predictions()` methods from `sklearn.metrics`.

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
```
