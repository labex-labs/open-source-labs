# Créer PrecisionRecallDisplay

De manière similaire, la courbe précision-rappel peut être tracée à l'aide de `y_score` de la section précédente.

```python
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

prec, recall, _ = precision_recall_curve(y_test, y_score, pos_label=clf.classes_[1])
pr_display = PrecisionRecallDisplay(precision=prec, recall=recall).plot()
```
