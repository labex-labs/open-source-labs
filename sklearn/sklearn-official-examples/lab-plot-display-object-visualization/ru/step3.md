# Создание RocCurveDisplay

Для построения ROC-кривой требуются либо вероятности, либо значения решений без порога от оценщика. Поскольку логистическая регрессия предоставляет функцию решения, мы будем использовать ее для построения ROC-кривой.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
