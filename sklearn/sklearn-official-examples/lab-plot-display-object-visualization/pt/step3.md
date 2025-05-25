# Criar RocCurveDisplay

A curva ROC requer probabilidades ou valores de decisão não limiarizados do estimador. Como a regressão logística fornece uma função de decisão, usaremos-a para plotar a curva ROC.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
