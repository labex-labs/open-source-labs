# Comparaison de la perte logarithmique

Nous comparons la perte logarithmique des classifieurs non étalonné et étalonné sur les prédictions des 1000 échantillons de test.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("Perte logarithmique de")
print(f" * classifieur non étalonné: {score:.3f}")
print(f" * classifieur étalonné: {cal_score:.3f}")
```
