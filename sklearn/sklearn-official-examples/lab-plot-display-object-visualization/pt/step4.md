# Criar PrecisionRecallDisplay

Analogamente, a curva precisão-revocação pode ser plotada usando `y_score` da seção anterior.

```python
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

prec, recall, _ = precision_recall_curve(y_test, y_score, pos_label=clf.classes_[1])
pr_display = PrecisionRecallDisplay(precision=prec, recall=recall).plot()
```
