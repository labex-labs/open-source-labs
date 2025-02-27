# RocCurveDisplay erstellen

Für die ROC-Kurve werden entweder die Wahrscheinlichkeiten oder die nicht schwellenwertbasierten Entscheidungswerte des Schätzers benötigt. Da die logistische Regression eine Entscheidungsfunktion liefert, werden wir sie verwenden, um die ROC-Kurve zu zeichnen.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
