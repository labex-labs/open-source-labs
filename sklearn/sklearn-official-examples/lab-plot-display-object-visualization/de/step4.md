# PrecisionRecallDisplay erstellen

Ähnlich kann die Genauigkeit-Erfassungsrate-Kurve mit `y_score` aus dem vorherigen Abschnitt geplottet werden.

```python
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

prec, recall, _ = precision_recall_curve(y_test, y_score, pos_label=clf.classes_[1])
pr_display = PrecisionRecallDisplay(precision=prec, recall=recall).plot()
```
