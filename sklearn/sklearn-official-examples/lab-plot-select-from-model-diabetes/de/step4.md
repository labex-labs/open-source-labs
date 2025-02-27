# Auswählen von Features mit sequentieller Featureauswahl

Wir verwenden den Sequential Feature Selector (SFS), um Features auszuwählen. SFS ist ein greedy-Verfahren, bei dem wir in jeder Iteration das beste neue Feature auswählen, das wir zu unseren ausgewählten Features hinzufügen möchten, basierend auf einem Kreuzvalidierungsscore. Wir können auch in die entgegengesetzte Richtung gehen (rückwärts SFS), d.h. beginnen wir mit allen Features und wählen schrittweise Features aus, die wir nacheinander entfernen möchten.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
