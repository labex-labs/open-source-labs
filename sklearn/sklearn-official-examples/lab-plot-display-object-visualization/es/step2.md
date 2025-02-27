# Crear ConfusionMatrixDisplay

Con el modelo ajustado, calculamos las predicciones del modelo en el conjunto de prueba. Estas predicciones se utilizan para calcular la matriz de confusión que se representa con `ConfusionMatrixDisplay`.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
