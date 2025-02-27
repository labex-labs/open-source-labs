# Crear RocCurveDisplay

La curva ROC requiere las probabilidades o los valores de decisión no umbralizados del estimador. Dado que la regresión logística proporciona una función de decisión, la usaremos para trazar la curva ROC.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
