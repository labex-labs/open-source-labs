# ConfusionMatrixDisplay erstellen

Mit dem trainierten Modell berechnen wir die Vorhersagen des Modells auf dem Testdatensatz. Diese Vorhersagen werden verwendet, um die Konfusionsmatrix zu berechnen, die mit `ConfusionMatrixDisplay` geplottet wird.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
