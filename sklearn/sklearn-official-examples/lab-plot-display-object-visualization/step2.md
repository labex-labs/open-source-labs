# Create ConfusionMatrixDisplay

With the fitted model, we compute the predictions of the model on the test dataset. These predictions are used to compute the confusion matrix which is plotted with the `ConfusionMatrixDisplay`.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
