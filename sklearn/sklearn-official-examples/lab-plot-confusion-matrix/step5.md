# Generate Confusion Matrix

We will generate a confusion matrix using the ConfusionMatrixDisplay class from scikit-learn. The confusion matrix will show the number of correct and incorrect predictions for each class.

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```
