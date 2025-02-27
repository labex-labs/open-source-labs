# Créer ConfusionMatrixDisplay

Avec le modèle ajusté, nous calculons les prédictions du modèle sur l'ensemble de test. Ces prédictions sont utilisées pour calculer la matrice de confusion qui est tracée avec `ConfusionMatrixDisplay`.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
