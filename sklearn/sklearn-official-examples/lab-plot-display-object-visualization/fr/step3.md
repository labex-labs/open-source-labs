# Créer RocCurveDisplay

La courbe ROC nécessite soit les probabilités soit les valeurs de décision non seuillées de l'estimateur. Étant donné que la régression logistique fournit une fonction de décision, nous l'utiliserons pour tracer la courbe ROC.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
